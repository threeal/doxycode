'''Test functions for parsing comments from a source code.'''

import pathlib
import unittest
from doxycode import parse_comments

class TestParse(unittest.TestCase):
    '''The unit testing class.'''

    def setUp(self):
        self.root = pathlib.Path(__file__).parent.resolve()

    def test_parse_comments(self):
        '''Test a function for parsing comments from a file.'''
        with open(self.root / "sample/include/sample/sample.hpp", 'r', encoding="utf-8") as file:
            comments = parse_comments(file)
            expected = ' namespace sample\n'
            self.assertEqual(comments, expected)

if __name__ == '__main__':
    unittest.main()
