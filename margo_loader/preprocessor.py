"""
    Process a notebook with nbdlang preamble
"""
from margo_parser import parser
import json
import re
import sys
import types


def preamble(source: str):

    """
    Return the all lines that begin with # :: at the start of the code cell
    """

    ret = ""

    for line in source.splitlines():
        # skip empty lines without breaking preamble
        if len(line.strip()) < 1:
            continue

        # we're done when we're past the # :: lines
        if line.strip().startswith("# ::"):
            ret += line.lstrip()[4:] + "\n"
        # skip comments without breaking preamble
        elif line.lstrip().startswith("#"):
            continue
        # We're done if it's not a comment or empty line
        else:
            break

    return ret


def parse_preamble(cell):
    return parser.parse(preamble(cell))


# TODO - This is is just a quick hack until I evaluate
# how to handle magics — which are valid IPython but not
# valid Python. Can/should I just execute all the code
# in IPython instead? For now, just sidestepping issue
def remove_magics(source):
    ret = ""
    for line in source.splitlines():
        if line.strip().startswith("%"):
            continue
        ret += line + "\n"
    return ret


def process_cell(cell):

    if cell.cell_type != "code":
        return (parse_preamble(""), "")

    try:
        preamble_instructions = parse_preamble(cell.source)
    except Exception as e:
        # Ignore invalid syntax
        raise Exception("Error parsing cell nbdlang:" + str(e))
        # preamble_instructions = []

    # ignore = False
    # for instruction in preamble_instructions:
    #     if instruction == "IGNORE_CELL":
    #         ignore = True

    # if ignore:
    #     return ([],"")

    return (preamble_instructions, remove_magics(cell.source))


def get_views(cell_preamble):
    ret = []
    for statement in cell_preamble["BODY"]:
        if statement["TYPE"] != "DECLARATION":
            continue
        if statement["NAME"] != "view":
            continue
        ret = ret + statement["VALUE"]

    return ret
    # ret = []
    # for instruction in cell_preamble:
    #     if not type(instruction) == tuple:
    #         continue
    #     if not len(instruction) == 2:
    #         continue
    #     if not instruction[0] == "view":
    #         continue
    #     # if not instruction[1][0].startswith("module."):
    #     #     continue
    #     for view_name in instruction[1]:
    #         if not type(view_name) == str:
    #             continue
    #         matches = re.match(r"module.(?P<submodule_name>[a-zA-Z0-9_\.]*)", view_name)
    #         if matches is None:
    #             continue
    #         submodule_name = matches.groupdict()["submodule_name"]

    #         if not len(submodule_name) > 0:
    #             continue

    #         ret.append(submodule_name)
    # return ret


def preamble_contains_ignore_cell(cell_preamble):
    for statement in cell_preamble["BODY"]:
        if (
            statement["TYPE"] == "BUILTIN"
            and statement["BODY"]["NAME"] == "IGNORE_CELL"
        ):
            return True
    return False


class Preprocessor:
    def __init__(self, module, name):
        self.module = module
        self.name = name

    def process_cells(self, cells):
        virtual_document = ""

        # If the first cell is a markdown cell, use it
        # as the module docstring
        if len(cells) > 0 and cells[0].cell_type == "markdown":
            self.module.__doc__ = cells[0].source

        for cell in cells:
            # virtual_document += process_cell(cell)
            cell_preamble, cell_source = process_cell(cell)

            # ignore-cell support
            # if "IGNORE_CELL" in cell_preamble:
            #     continue
            if preamble_contains_ignore_cell(cell_preamble):
                continue

            # view: module.view_name support ::
            views = get_views(cell_preamble)
            for view in views:
                full_view_name = self.name + "." + view

                if full_view_name in sys.modules:
                    mod = sys.modules[full_view_name]

                else:
                    mod = types.ModuleType(full_view_name)
                    sys.modules[full_view_name] = mod
                exec(cell_source, mod.__dict__)
                # TODO - This version does not do it, but I should
                # probably execute every cell in a view. Cells
                # without a view specified should run in a default
                # view, and then that view should be assigned to the main
                # module at the end
                self.module.__dict__[view] = mod

            exec(cell_source, self.module.__dict__)

        # exec(virtual_document, self.module.__dict__)
