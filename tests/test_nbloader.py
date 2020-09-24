import unittest


class TestImports(unittest.TestCase):

    def test_nbdmod_can_load(self):
        from nbdmod import nbloader

    def test_nbdmod_imports_cells(self):
        # from nbdmod import nbloader
        from test_notebooks import hello_notebook

        self.assertEqual(hello_notebook.should_export, 200)        

    def test_nbdmod_imports_single_variables(self):
        from test_notebooks.hello_notebook import should_export
        self.assertEqual(should_export, 200)
        
if __name__ == '__main__':
    unittest.main()
