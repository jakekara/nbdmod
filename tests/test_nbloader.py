def test_can_load():
    from nbdmod import nbloader


def test_imports_cells():
    # from nbdmod import nbloader
    from test_notebooks import hello_notebook

    assert hello_notebook.should_export == 200


def test_imports_single_variables():
    from test_notebooks.hello_notebook import should_export

    assert should_export == 200


def test_imports_ipynb_docstring():
    from test_notebooks import hello_notebook

    assert hello_notebook.__doc__.startswith("# A regular notebook")
