import margo_loader  # noqa: F401


def test_start_and_stop():
    from test_notebooks import start_and_stop

    assert not hasattr(start_and_stop, "three")
    assert not hasattr(start_and_stop, "two")
    assert not hasattr(start_and_stop, "one")

    assert hasattr(start_and_stop, "four")
    assert hasattr(start_and_stop, "five")
    assert hasattr(start_and_stop, "six")

    assert start_and_stop.four == 4
    assert start_and_stop.five == 5
    assert start_and_stop.six == 6
