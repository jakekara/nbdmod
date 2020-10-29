from margo_loader.preprocessor import preamble


def test_processes_empty_soure():
    assert preamble("") == ""


def test_processes_source_without_preamble():
    assert (
        preamble(
            """
    # This should not be captured
    # This should not be captured either
    print('hello, world')
    """
        )
        == ""
    )


def test_does_not_capture_nbdl_syntax_after_preamble():
    assert (
        preamble(
            """
    # This should not be captured
    print('hello, world')
    # :: This should also not be captured ::
    """
        )
        == ""
    )


def test_preamble_captures_preamble():
    assert preamble("# :: Get this ::") == " Get this ::\n"


def test_preamble_captures_preamble_and_excludes_comments():
    source = """

    # :: Get this ::
    # Don't get this
    """

    assert preamble(source) == " Get this ::\n"


def test_allowed_comments_in_preamble():
    assert (
        preamble(
            """
    # This is a comment
    # Comment's shouldn't interrupt the preamble
    # :: Get this ::
    # :: Get this, too ::
    # Don't get this

    print('preamble over)
    """
        )
        == " Get this ::\n Get this, too ::\n"
    )
