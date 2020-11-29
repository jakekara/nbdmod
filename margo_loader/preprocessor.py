"""
    Process a notebook with nbdlang preamble
"""
# from margo_parser import parser
from margo_parser.api.get_preamble_block import get_preamble_block
from margo_parser.api.MargoBlock import MargoBlock
from margo_parser.api.MargoStatement import MargoStatementTypes
import json
import re
import sys
import types


# def preamble(source: str):

#     """
#     Return the all lines that begin with # :: at the start of the code cell
#     """

    # ret = ""

    # for line in source.splitlines():
    #     # skip empty lines without breaking preamble
    #     if len(line.strip()) < 1:
    #         continue

    #     # we're done when we're past the # :: lines
    #     if line.strip().startswith("# ::"):
    #         ret += line.lstrip()[4:] + "\n"
    #     # skip comments without breaking preamble
    #     elif line.lstrip().startswith("#"):
    #         continue
    #     # We're done if it's not a comment or empty line
    #     else:
    #         break

    # return ret


# def parse_preamble(cell):
    # return margo.b
    # return parser.parse(preamble(cell))


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


def process_cell(cell) -> (MargoBlock, str):

    print("CELL_TYPE:", cell.cell_type)

    if cell.cell_type != "code":
        return (get_preamble_block(""), cell.source)

    return (
        get_preamble_block(cell.source), 
        remove_magics(cell.source)
    )


def get_views(cell_preamble: MargoBlock):
    ret = []
    for statement in cell_preamble.statements:
        if statement.type != MargoStatementTypes.DECLARATION:
            continue
        if statement.name != "view":
            continue
        ret = ret + statement.value

    return ret


def preamble_contains_ignore_cell(cell_preamble: MargoBlock):
    for statement in cell_preamble.statements:
        if (
            statement.type == MargoStatementTypes.DIRECTIVE
            and statement.name == "ignore-cell" 
        ):
            return True
    return False


class Preprocessor:
    def __init__(self, module, name):
        self.module = module
        self.name = name

    def process_cells(self, cells):
        virtual_document = ""

        idx = -1
        for cell in cells:
            idx += 1
            # If the first cell is a markdown cell, use it
            # as the module docstring
            if idx == 0 and cell.cell_type == "markdown":
                self.module.__doc__ = cell.source
                
            # virtual_document += process_cell(cell)
            cell_preamble, cell_source = process_cell(cell)
            print("process_cell() returned", process_cell(cell))

            # ignore-cell support
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

            if (cell.cell_type == "code"):
                exec(cell_source, self.module.__dict__)
