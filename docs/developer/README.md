# margo-loarder developer documentation

## Setting up your environment

Set up a virtual environment. I like to use `mkvirtualenv`.

Then install the developer requirements:

```bash
pip install -r requirements-dev.txt
```

Then install the package in an editable form:

```bash
pip install -e .
```

## Using tox

This project uses tox to automate linting, formatting and testing.

To run tox, use:

```bash
tox
```

You should see something like:

```
tests: recreate env because python changed version_info=[3, 11, 2, 'final', 0]->[3, 9, 16, 'final', 0] | executable='/usr/local/bin/python3.11'->'/usr/local/bin/python3.9'
tests: remove tox env folder /app/.tox/tests
tests: install_deps> python -I -m pip install -r requirements-dev.txt
.pkg: recreate env because python changed version_info=[3, 11, 2, 'final', 0]->[3, 9, 16, 'final', 0] | executable='/usr/local/bin/python3.11'->'/usr/local/bin/python3.9'
.pkg: remove tox env folder /app/.tox/.pkg
.pkg: install_requires> python -I -m pip install hatch-requirements-txt hatchling
.pkg: _optional_hooks> python /usr/local/lib/python3.9/site-packages/pyproject_api/_backend.py True hatchling.build
.pkg: get_requires_for_build_sdist> python /usr/local/lib/python3.9/site-packages/pyproject_api/_backend.py True hatchling.build
.pkg: prepare_metadata_for_build_wheel> python /usr/local/lib/python3.9/site-packages/pyproject_api/_backend.py True hatchling.build
.pkg: build_sdist> python /usr/local/lib/python3.9/site-packages/pyproject_api/_backend.py True hatchling.build
tests: install_package_deps> python -I -m pip install 'margo-parser<2,>=1' nbformat==5.0.7
tests: install_package> python -I -m pip install --force-reinstall --no-deps /app/.tox/.tmp/package/2/margo_loader-1.0.1.tar.gz
tests: commands[0]> python -m pytest
================================================= test session starts ==================================================
platform linux -- Python 3.9.16, pytest-7.2.2, pluggy-1.0.0
cachedir: .tox/tests/.pytest_cache
rootdir: /app
collected 18 items                                                                                                     

tests/test_do_not_import.py .                                                                                    [  5%]
tests/test_get_nby_cells.py .                                                                                    [ 11%]
tests/test_nbloader.py .....                                                                                     [ 38%]
tests/test_nbloader_with_nbpy_files.py ...                                                                       [ 55%]
tests/test_resolve_path.py ......                                                                                [ 88%]
tests/test_start_and_stop.py .                                                                                   [ 94%]
tests/test_views.py .                                                                                            [100%]

================================================== 18 passed in 2.00s ==================================================
.pkg: _exit> python /usr/local/lib/python3.9/site-packages/pyproject_api/_backend.py True hatchling.build
  tests: OK (89.03=setup[86.23]+cmd[2.80] seconds)
  congratulations :) (89.15 seconds)
```

## Running tests with docker-compose

To run tox in docker-compose, use:

```bash
docker-compose run py39
```

Replace py39 with any of: `py36`, `py37`,`py38`, `py39`, `py310`, `py311` to run
tests in different versions of python.