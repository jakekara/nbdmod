# margo-loader

Import notebooks in Python using [Margo notebook margin
syntax](https://github.com/jakekara/nbdl).

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

## Using margo to improve notebook portability

In your notebook file, you can mark a cell so that it is not imported by the
`import` statement.

```python
# :: ignore-cell ::
print("This code will not be executed when imported with margo-loader")
```

This little bit of syntax makes this library much different and more useful than
past examples of tools that merely import an entire notebook as if it were a
`.py` file. Because of their interactive nature, Notebooks may contain code that
doesn't make sense to import elsewhere, and that's what the `ignore-cell`
statement addresses.

## A note about the comment syntax

That `# ::` signifies that the rest of the line is going to be written in a
special syntax called margo syntax. The syntax is very lightweight, it's meant
to be extended by projects like nbdmod. The Python reference interpreter is maintained in a separate repostitory [here](https://github.com/jakekara/nbdl/).

## view: Creating virtual submodules

Another feature of margo-loader is that you can create virtual submodules within
a notebook. This in effect allows you to import different groups of cells from
the same notebook. Here's an example borrowed from the file
`test_notebooks/greetings.ipynb` in this repo.

```python
# greetings.ipynb cell 1
# :: view: "grumpy" ::
def say_hello(to="world"):
    return f"Oh, uhh, hi {to}..."
```

```python
# greetings.ipynb cell 2
# :: view: "nice" ::
def say_hello(to="world"):
  return f"Hello, {to}! Nice to see you."
```

Notice we define the same `say_hello` function twice. If the entire notebook
were imported, the second `say_hello` would overwrite the first. However, we can
import either of these submodule views using Python's standard import syntax once we import `margo_loader`.

```python
from greetings import nice, grumpy
nice.say_hello()
>>> "Hello, world! Nice to see you."
grumpy.say_hello()
>>> "Oh, uhh, hi world..."
```

This allows for multiple "views" of the same source code module, as defined in
[Calliss 1991, A comparison of module constructs in programming
languages](https://dl.acm.org/doi/10.1145/122203.122206)

## The view statement is a reserved declaration name

The `view` statement is not actually built into margo syntax. You won't find it
in the margo-parser code. Margo syntax allows users to declare variables with
any name with the following syntax:

```python
# :: {variable name}: {list of values} ::
```

This project, margo-loader, reserves the `view` name to add the functionality
described above. For this reason we consider it a reserved keyword, but it is a
loose definition. Other tools may make use of margo-parser but have no use for
the `view` keyword and not treat it differently from any other named value.

## Specially formatted declarations

The `view` syntax above accepts a list of strings that are view names. Margo
syntax allows for declarations to be provided as valid JSON, YAML or plain text
strings as well.

You can specify the format like so:

```python
# :: {variable_name} [{format}]: {string}
```

The `test_notebooks/requirements.ipynb` file in this repository demonstrates why
you might want to use raw variable declarations. In that notebook, we have code like this

```python
# :: requirements.txt [raw]: '
# :: dep
# :: dep-a b c
# :: dep 3
# :: ' ::
```

This declares a variable named `requirements.txt` in the raw (plain) text format
and includes a list of Python packages (well fake ones). The idea is that you
can define a notebook's dependencies right at the top, or dispersed throughout
the notebook. But what good is this? We need a tool to be able to extract this information to a plain requirements.txt file. Fortunately margo-loader provides a CLI tool for that

```python
$ python -m margo_loader.cli extract -i test_notebooks/requirements.ipynb -f raw -p requirements.txt

 dep
 dep-a b c
 dep 3

...
```

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
described above, my project aims to build upon this with the addition of margo
syntax for preprocessing. I believe these enhancements address the reason that
example has largely been abandoned.
