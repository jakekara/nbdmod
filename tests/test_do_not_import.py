import margo_loader  # noqa: F401
import pytest


def test_do_not_import():
    with pytest.raises(Exception):
        from test_notebooks import do_not_import_me  # noqa: F401
