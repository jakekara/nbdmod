# margo-loader

> Import computational Jupyter Notebooks notebooks as Python modules, with
> support for Margo syntax.

## Installation

To install margo-loader, run:

```bash
pip install git+https://github.com/jakekara/nbmod
```

## Importing a notebook

Assuming you have a file called "notebook.ipynb" somewhere in your import path:

```python
import margo_loader
import notebook
```

## Why this approach is different

Previous attempts have been made to make notebooks importable like normal Python
source files. While these attempts work just fine, they do not account for a
non-technical problem: Notebook code is written differently from modular code,
so it often includes a lot of code you don't want to run when you import it
outside of the original notebook context.

This loader works largely the same as those past projects, but it adds support
for Margo, a lightweight syntax for annotating notebooks with extra information.

If you want to prevent a cell from being exported, start your cell with the specially-formatted comment line `# :: ignore-cell ::`, like this:

```python
# :: ignore-cell ::
print("This code will not be executed when imported with margo-loader")
```

This special code comment is called a Margo note. Margo notes in Python cells begin with `# ::` to differentiate them from regular comments, and end with `::`.

Learn more about the underlying Margo syntax [here](https://github.com/jakekara/nbdl/).

## Creating virtual submodules

Another feature of margo-loader is that you can create virtual submodules within
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
import either of these submodules using Python's standard import syntax once we
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

The concept of programming with multiple views of the same source code is
articulated well in [Calliss 1991, A comparison of module constructs in
programming languages](https://dl.acm.org/doi/10.1145/122203.122206)

## Working with percent-formatted notebooks

This library works with Jupyter Notebooks (.ipynb files) as well as python files
with percent cell formatting using the file extension `.pynb`. These are plain
source Python files that use `# %%` to split the document into cells. [Read more
here](https://code.visualstudio.com/docs/python/jupyter-support-py).

Look at `test_notebooks/hello_notebook_pynb.pynb` in this repo for an example of
a code-cell notebook.

**STABILITY NOTE: This is an alpha feature. The .pynb extension may be changed in a future version**

## Prior art

This project borrows code and implementation approach from [a Jupyter Notebook
documentation
example](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Importing%20Notebooks.html)
that imports notebooks in their entirety as if they were `.py` files. As
described above, my project aims to build upon this with the addition of margo
syntax for preprocessing. I believe these enhancements address the reason that
example has largely been abandoned.
