import pytest

from nbdmod.preprocessor import parse_preamble



def test_can_process_empty_preamble():
    assert parse_preamble(
        """
        print('hello')
        """
    ) == []

def test_invalid_preamble_raises():
    with pytest.raises(Exception):
        parse_preamble(
            """
            #: ignore-cell
            """
        )

def test_valid_preamble_parses():
    assert parse_preamble("""
    #: ignore-cell ::
    """) == ["IGNORE_CELL", "END_BLOCK"]
