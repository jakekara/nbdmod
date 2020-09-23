
import io
import sys
import types
from nbformat import read
from IPython.core.interactiveshell import InteractiveShell
from IPython import get_ipython

from .find_notebook import find_notebook

class NotebookLoader(object):
    """Module Loader for Jupyter Notebooks"""
    def __init__(self, path=None):
        self.shell = InteractiveShell.instance()
        self.path = path

    def load_module(self, fullname):
        """import a notebook as a module"""
        path = find_notebook(fullname, self.path)

        # load the notebook object
        with io.open(path, 'r', encoding='utf-8') as f:
            nb = read(f, 4)

        # create the module and add it to sys.modules
        # if name in sys.modules:
        #    return sys.modules[name]
        mod = types.ModuleType(fullname)
        mod.__file__ = path
        mod.__loader__ = self
        mod.__dict__['get_ipython'] = get_ipython
        sys.modules[fullname] = mod

        # extra work to ensure that magics that would affect the user_ns
        # actually affect the notebook module's ns
        save_user_ns = self.shell.user_ns
        self.shell.user_ns = mod.__dict__

        virtual_document = ""
        try:
          for cell in nb.cells:
            if cell.cell_type == 'code':

                if (cell.source.startswith("#NBMODULE_IGNORE")):
                    continue

                # append the code to document
                virtual_document = virtual_document + cell.source + "\n"
        finally:
            pass
            # self.shell.user_ns = save_user_ns

        exec(virtual_document, mod.__dict__)
        # self.shell.user_ns = save_user_ns 

        return mod