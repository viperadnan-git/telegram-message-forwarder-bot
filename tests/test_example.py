import unittest


class ExampleTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        self.assertEqual("string" + None, "string",
                         'append None to string equals argument')

if __name__ == '__main__':
    unittest.main()