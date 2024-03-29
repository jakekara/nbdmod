# margo-loader

> Import Jupyter Notebooks notebooks as Python modules

## Video tutorial

[Live Coding Demo: Using Jupyter Notebooks as Python Modules with Margo Loader](https://www.youtube.com/watch?v=6EgsAb56jY0).

## Demo Notebooks  

Want to see Margo Loader in action before installing it? Here's a live [demo notebook](https://colab.research.google.com/drive/1X1vuPRrj7SOpGl71wFCwFNgX40W18Kyl#scrollTo=WyrdS8A06eA6) on Google Colaboratory.

A more realistic suite of notebooks for background deletion and color extraction on William Blake prints is available in this [Binder](https://mybinder.org/v2/zenodo/10.5281/zenodo.4554402/) VM, which runs in a browser without installation.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/zenodo/10.5281/zenodo.4554402/)

## Installation

To install margo-loader, run:

```bash
pip install git+https://github.com/margo-notebooks/margo-loader-py
```

## Importing a notebook

Assuming you have a file called "notebook.ipynb":

```python
import margo_loader
import notebook
```

## ignore-cell

Not every cell in a Notebook makes sense to include in its module representation.

If you want to prevent a cell from being exported, start the cell with the specially-formatted comment line `# :: ignore-cell ::`, like this:

```python
# :: ignore-cell ::
print("This code will not be executed when imported with margo-loader")
```

This special code comment is called a Margo note. Margo notes in Python cells begin with `# ::` to differentiate them from regular comments, and end with `::`.

Learn more about the underlying Margo syntax [here](https://github.com/jakekara/nbdl/).

An alias for `ignore-cell` is `skip`. So this does the same thing:

```python
# :: skip ::
print("This code will not be executed when imported with margo-loader")
``` 
## Creating virtual submodules

You can organize code cells into virtual submodules within
a notebook. This in effect allows you to group cells from the same notebook.
Here's an example of a few cells from the file
`test_notebooks/greetings.ipynb` in this repo.

```python
# greetings.ipynb
# :: submodule: "grumpy" ::
def say_hello(to="world"):
    return f"Oh, uhh, hi {to}..."
```

```python
# greetings.ipynb
# :: submodule: "nice" ::
def say_hello(to="world"):
  return f"Hello, {to}! Nice to see you."
```

Notice we define the same `say_hello` function twice. If the entire notebook
were imported, the second `say_hello` would overwrite the first. However, we can
import either of these submodules or both using Python's standard import syntax once we
import `margo_loader`.

```python
>>> import margo_loader
>>> from test_notebooks.greetings import nice, grumpy
>>> nice.say_hello()
'Hello, world! Nice to see you.'
>>> grumpy.say_hello()
'Oh, uhh, hi world...'
>>>
```

## Prevent a notebook from being imported

To prevent a notebook from being imported, use:

```python
# :: not-a-module ::
```

or 

```python
# :: do-not-import ::
```

These are currently aliases with the same behavior. If you try to import a notebook that contains a `do-not-import`/`not-a-module` declaration, it will raise an exception.

## Skipping multiple cells

If you want to ignore a lot of cells during import, you can use


```python
# :: module-stop ::
```

and

```python
# :: module-start :: 
```

to exclude blocks of cells.

Any cell including and after a cell that contains `module-stop` will be excluded during import until a `module-start` cell is encountered.

Conversely, any cell including and after a cell that contains `module-start` will be excluded during import until a `module-stop` is encountered.

Note that you can also use `start` and `stop` instead of `module-start` and `module-stop`. These are aliases.

You can use `module-stop` with no subsequent `module-start`. This will have the effect of ignoring all subsequent cells.

## Working with percent-formatted notebooks

This library works with Jupyter Notebooks (.ipynb files) as well as python files
with percent cell formatting using the file extension `.pynb`. These are plain
source Python files that use `# %%` to split the document into cells. [Read more
here](https://code.visualstudio.com/docs/python/jupyter-support-py).

Look at `test_notebooks/hello_notebook_pynb.pynb` in this repo for an example of
a code-cell notebook.

**STABILITY NOTE:** *This is an alpha feature. The .pynb extension may be changed in a future version*

## Prior art

This project borrows its implementation approach from [a Jupyter Notebook
documentation
example](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Importing%20Notebooks.html)
that imports notebooks in their entirety as if they were `.py` files. The key difference Margo Loader adds is use of Margo notes to create preoprocessor directives  `ignore-cell` and `submodule`.

## Development quick-start

To get started developing Margo in a virutal env, run:

```bash
python -m venv venv
. ./venv/bin/activate
pip install -r requirements
python setup.py develop
pytest
```
