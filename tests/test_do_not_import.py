import margo_loader
import pytest

def test_do_not_import():
    with pytest.raises(Exception):
        from test_notebooks import do_not_import_me
