import sys
import types

from .utils.resolve_path import resolve_multiple_extensions
from .preprocessor import Preprocessor
from .utils.get_cells.get_cells import get_cells

class NotebookLoader(object):

    """Module Loader for Jupyter Notebooks"""

    def __init__(self, path=None, target=None):
        self.path = path
        self.target = target

    def load_module(self, fullname):
        """import a notebook as a module"""

        path = resolve_multiple_extensions(fullname, path=self.path)


        # don't do anything if module is loaded
        if fullname in sys.modules:
           return sys.modules[fullname]

        # create the module and add it to sys.modules
        mod = types.ModuleType(fullname)
        mod.__file__ = path
        mod.__loader__ = self

        cells = get_cells(path)
        try:
            processor = Preprocessor(mod)
            processor.process_cells(cells)
        except Exception as e:
            raise ImportError("Failed to process cells: " + e)

        # Add the module to sys.modules
        sys.modules[fullname] = mod

        return mod
