# margo-loader

Import notebooks in Python using [Margo notebook margin
syntax](https://github.com/jakekara/nbdl). Not just Jupyter Notebooks, it also
imports Python files that use percent format (`# %%`) code cells)

## Install and develop

While in development, this must be installed from github repos

```bash
git clone git@github.com:jakekara/nbdmod.git
cd nbdmod
python setup.py develop
```

## Usage

Assuming you have a file called "notebook.ipynb" somewhere in your import path:

```python
from nbdmod import nbloader
import notebook
```

## Using margo to improve notebook portability

In your notebook file, you can mark a cell so that it is not imported by the
`import` statement.

```python
# :: ignore-cell ::
print("This code will not be executed when imported with nbmod")
```

This little bit of syntax makes this library much different and more useful than
past examples of tools that merely import an entire notebook as if it were a
`.py` file. That's because notebooks are not written to be modules, so they
include code that isn't "re-usable," like generating charts, performing one-time
computations on specific data sets.

That `# ::` signifies that the rest of the line is going to be written in a
special syntax called [nbdlang](https://github.com/jakekara/nbdl/), a related
project for describing notebook code, which among other things can tell
interpreters to ignore a code cell.

## nbdlang support status

Not all nbdlang syntax is meaningful to the `import` mechanism. The following
syntax features will be implemented by this library

### ignore-cell

This directive excludes the cell's contents during the import, so it is wholly
ignored by the importing code. This is great to use on one-time computations in
notebooks which don't make sense outside of the notebook context.

Example:

```python
# :: ignore-cell ::
```

### view: {view_name}

This executes a code's cell inside a dynamically defined module named
`{view_name}` during the import.

Let's say this code was inside a notebook called "hhgtg.ipynb"...

```python
# :: view: module.philosophy
meaning_of_life = 42
```

Now you can access just the cells marked as belonging to the philosophy
submodule with the following:

```python
>>> from hhgtg import philosophy
>>> print philosophy.meaning_of_life
```

This allows for multiple "views" of the same source code module, as defined in
[Calliss 1991, A comparison of module constructs in programming
languages](https://dl.acm.org/doi/10.1145/122203.122206)

**Note:** For now, code that is marked with views is still considered part of
the root module as well as the virtual submodule. So you will see
`meaning_of_life` exists both in `hhgtg` and `hhgtg.philosophy`

```python
>>> import hhgtg
>>> hhgtg.philosophy.meaning_of_life
42
>>> hhgtg.meaning_of_life
42
```

This doesn't feel like the best solution, but if every cell with a view tag is
removed entirely from the root notebook context, this could require a lot more
markup on the part of notebook developers. So I'm not sure what the best
solution is yet. One option is the create a notebook context that includes every
cell, a module cell that includes every cell not marked with `ignore-cell` and
create any user-defined submodules that contain only the cells explicity marked
with one or more `view` tags.

## Working with "# %%" code cells

This library works with Jupyter Notebooks (.ipynb files) as well as python files
with vscode code cells using the file extension `.pynb`. These are plain source
Python files that use "# %%" to split the document into cells. [Read more
here](https://code.visualstudio.com/docs/python/jupyter-support-py).

Look at `test_notebooks/hello_notebook_pynb.pynb` in this repo for an example of
a code-cell notebook.

## Prior art

This project borrows code and implementation approach from [a Jupyter Notebook
documentation
example](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Importing%20Notebooks.html)
that imports notebooks in their entirety as if they were `.py` files. As
described above, my project aims to build upon this with the addition of nbdlang
preprocessing.
