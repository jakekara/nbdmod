# nbdmod

Import notebooks in Python using nbdlang (notebook description language).

This works with Jupyter Notebooks (.ipynb files) as well as python files with
vscode code cells using the file extension `.pynb`. These are plain source
Python files that use "# %%" to split the document into cells. [Read more
here](https://code.visualstudio.com/docs/python/jupyter-support-py).

## Usage

If you have a file called "notebook.ipynb" somewhere you can import it.

```python
from nbdmod import nbloader
import notebook
```

That's it.

For examples look in the test_notebooks directory. (Copy them rather than
altering these files, because the tests use these files and will fail if you
edit them.)

## Support for nbdlang syntax

Only certain nbdlang directives are relevant to the process of importing
notebooks.

### ignore-cell (Implemented)

This directive excludes the cell's contents during the import, so it is wholly
ignored by the importing code. This is great to use on one-time computations in
notebooks which don't make sense outside of the notebook context.

```python
#: ignore-cell ::
print("This code will not be executed when imported with nbmod")
```

### view: {view_name} (Not implemented)

This executes a code's cell inside a programmatically defined module named
`{view_name}` during the import.

Let's say this code was inside a notebook called "hhgtg.ipynb"...

```python
#: view: philosophy
meaning_of_life = 42
```

... and you import it with ...

```python
import hhgtg
```

... the `hhgtg.meaning_of_life` variable will not be defined as it normally
would. Instead it will be defined in `hhgtg.philosophy.meaning_of_life`.

This allows for multiple "views" of a module, as defined in [Calliss 1991, A
comparison of module constructs in programming
languages](https://dl.acm.org/doi/10.1145/122203.122206)

## Method

Code adapted from here:
https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Importing%20Notebooks.html

This approach has struggled to gain general use. I think that's mainly because
notebook code is not currently written to be imported elsewhere. There are often
cells that do not make sense to execute outside of the notebook context (in the
module context). With [nbdlang](https://github.com/jakekara/nbdl/), we can use
`ignore-cell` and other syntax features to describe how notebooks should be
imported.
