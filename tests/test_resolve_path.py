from margo_loader.utils.resolve_path import resolve_path
from margo_loader.utils.resolve_path.LEGACY_find_notebook import find_notebook


def test_does_not_find_nonexistent_file():
    assert resolve_path("Hello") is None


def test_does_not_find_dotpy_file():
    assert resolve_path("hello", path=["test_notebooks"]) is None


def test_does_find_nbpy_file():
    resolved_path = resolve_path("hello_notebook_nbpy", path=["test_notebooks"])
    expected_path = "test_notebooks/hello_notebook_nbpy.nbpy"
    assert resolved_path == expected_path


def test_does_not_find_ipynb_if_not_looking():
    assert resolve_path("hello_notebook", path=["test_notebooks"]) is None


def test_does_find_ipynb_file():
    resolved_path = resolve_path(
        "hello_notebook", path=["test_notebooks"], ext="ipynb"
    )
    expected_path = "test_notebooks/hello_notebook.ipynb"
    assert resolved_path == expected_path


def test_results_match_legacy_code():
    assert resolve_path(
        "hello_notebook_nbpy", path=["test_notebooks"]
    ) == find_notebook("hello_notebook_nbpy", ["test_notebooks"])
    assert resolve_path("hello_notebook_nbpy") == find_notebook(
        "hello_notebook_nbpy"
    )
