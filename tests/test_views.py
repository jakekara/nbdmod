import margo_loader  # noqa: F401


def test_imports_both_views():
    from test_notebooks import greetings

    assert greetings.say_hello() == "Hello, world! Nice to see you."
    assert greetings.grumpy.say_hello() == "Oh, uhh, hi world..."
    assert greetings.nice.say_hello() == "Hello, world! Nice to see you."
