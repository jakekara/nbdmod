from margo_loader.utils.get_cells.get_nbpy_cells import get_cells


def test_gets_cells():
    cells = get_cells("./test_notebooks/hello_notebook_nbpy.nbpy")
    assert len(cells) == 4
    expected = (
        "# :: ignore-cell ::\n# This code should not "
        + "be executed\nshould_export = 500\n"
    )
    assert cells[-1].source == expected
