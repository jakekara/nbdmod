# Support for the view syntax

Create virtual submodules using the syntax:

```python
# :: view: module.{submodule-name} ::
```

## Status

Implemented, but see [considerations](#considerations) below.

## Example usage

In a greetings.ipyb, we would have the following two cells:

```python
# :: view: module.nice ::

def say_hello(to="world"):
  print(f"Hello, {to}! Nice to see you.")
```

```python
# :: view: module.grumpy ::

def say_hello(to="world"):
printf(f"Oh, uhh, hi {to}...")
```

To use this notebook, we use `from {path}.{to}.{notebook} import {view_name}`,
which is to say:

```python
>>> from greetings.grumpy import say_hello
>>> say_hello("jake")
"Oh, uhh, hi jake..."
>>> from greetings.nice import say_hello
"Hello, jake! Nice to see you."
```

## Implementation

The cell processor looks for valid metadata assignment tuples that assign to the
reserved word `view`.

If any are found, all string values in the value list are processed as potential
view names. They must be prefixed with `module.` for now.

For each valid assignment, the value after `module.` is used as the
`submodule_name`. The submodule is created dynamically using Types.module, the
cell source is executed inside that module's `__dict__` namespace, and then the
module is assigned to the name `submodule_name` in the root of the notebook
module.

## Example

For an example of a notebook that declares submodules, see
`test_notebooks/greetings.ipynb` in this repo.

For a corresponding example of that notebook being imported, look at
`tests/test_views.py` in this repo.

## Considerations

**Should deep submodules be allowed?**

Should you be able to use syntax like:

`view: a.b.c.d`

Or should we not allow dots in the `submodule_name`?

**Is a view meant to limit the visibility of code?**

This is a tricky one. We can use `ignore-cell` to make a cell entire invisible.
It is always ignored under the current definition. But submodule views pose a
question. When a cell is marked to belong to a submodule view, should it be
executed both in the root module and the specified submodule, or should it only
be executed in the specified submodule?

Stated another way, would a user use these virtual submodules to isolate code,
or to create additional different views that contain some subset of the entire
module?

The current implementation executes the cell source both in the root module and
in the virtual submodule.
