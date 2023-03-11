Module margo_loader.utils.resolve_path.LEGACY_find_notebook
===========================================================

Functions
---------

    
`find_notebook(fullname, path=None)`
:   find a notebook, given its fully qualified name and an optional path
    
    This turns "foo.bar" into "foo/bar.ipynb"
    and tries turning "Foo_Bar" into "Foo Bar" if Foo_Bar
    does not exist.