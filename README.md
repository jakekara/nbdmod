# nbdmod

Import notebooks in Python using nbdlang (notebook description language).

## Usage

If you have a file called "notebook.ipynb" somewhere you can import it.

```python
from nbdmod import nbloader
import notebook
```

That's it.

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

This allows for multiple "views" of a module, as defined in [Calliss 1991, A comparison of module constructs in programming languages](https://dl.acm.org/doi/10.1145/122203.122206)

## Method

Code adapted from here:
https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Importing%20Notebooks.html

This approach has struggled to gain ground as a useful tool, and I submit that's
because it is not useful to simply import notebooks. There needs to be a
language to describe how they are imported.
