def test_nbdmod_can_load():
    import margo_loader  # noqa: F401


def test_nbdmod_imports_cells():
    from test_notebooks import hello_notebook_nbpy as hello_notebook

    assert hello_notebook.should_export == 200


def test_nbdmod_imports_single_variables():
    from test_notebooks.hello_notebook_nbpy import should_export

    assert should_export == 200
