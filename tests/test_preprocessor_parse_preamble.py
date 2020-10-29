import pytest

from nbdmod.preprocessor import parse_preamble


def test_can_process_empty_preamble():
    parsed = parse_preamble(
            """
        print('hello')
        """
    )

    assert parsed["BODY"] == []

def test_invalid_preamble_raises():
    with pytest.raises(Exception):
        parse_preamble(
            """
            # :: ignore-cell
            """
        )


def test_valid_preamble_parses():
    parsed = parse_preamble("""
    # :: ignore-cell ::
    """
    )
    assert type(parsed) == dict
    assert parsed["BODY"][0]["TYPE"] == "BUILTIN"
    assert parsed["BODY"][0]["BODY"]["NAME"] == "IGNORE_CELL"
        

