import unittest


class TestImports(unittest.TestCase):

    def test_cogsly_can_load(self):
        from cogsly import nbloader

    def test_cogsly_imports_cells(self):
        from cogsly import nbloader
        from test_notebooks import hello_notebook

        self.assertEqual(hello_notebook.should_export, 200)        

if __name__ == '__main__':
    unittest.main()
