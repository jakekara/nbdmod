"""
    Process a notebook with nbdlang preamble
"""
from notebook_description_language import parser
import json


def preamble(source: str):

    """
    Return the all lines that begin with #: at the start of the code cell
    """

    ret = ""

    for line in source.splitlines():
        # skip empty lines without breaking preamble
        if len(line.strip()) < 1:
            continue

        # we're done when we're past the #: lines
        if line.strip().startswith("#:"):
            ret += line.lstrip()[2:] + "\n"
        # skip comments without breaking preamble
        elif line.lstrip().startswith("#"):
            continue
        # We're done if it's not a comment or empty line
        else:
            break

    return ret


def parse_preamble(cell):
    return parser.parse(preamble(cell))


def process_cell(cell):

    if cell.cell_type != "code":
        return ""

    # old way works but not extensible
    # if cell.source.startswith("#: ignore-cell ::"):
    #     return ""
    try:
        preamble_instructions = parse_preamble(cell.source)
    except:
        # Ignore invalid syntax
        preamble_instructions = []

    IGNORE = False
    for instruction in preamble_instructions:
        if instruction == "IGNORE_CELL":
            IGNORE = True

    if IGNORE:
        return ""

    return cell.source + "\n"


class Preprocessor:
    def __init__(self, module):
        self.module = module

    def process_cells(self, cells):
        virtual_document = ""

        for cell in cells:
            virtual_document += process_cell(cell)

        exec(virtual_document, self.module.__dict__)
