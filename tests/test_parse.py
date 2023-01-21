'''Test functions for parsing comments from a source code.'''

import json
import pathlib
import unittest
from doxycode import parse_comments

class TestParse(unittest.TestCase):
    '''The unit testing class.'''

    def setUp(self):
        self.root = pathlib.Path(__file__).parent.resolve()
        self.source_dir = self.root / 'sample/include'
        self.expected_dir = self.root / 'sample/expected'

    def test_parse_comments(self):
        '''Test a function for parsing comments from a file.'''
        with open(self.source_dir / 'sample/sample.hpp', 'r', encoding='utf-8') as file:
            comments = parse_comments(file)
            expected_file = self.expected_dir / 'sample/sample_comments.json'
            with open(expected_file, 'r', encoding='utf-8') as file:
                file_txt = file.read()
                expectations = json.loads(file_txt)
                self.assertEqual(comments, expectations)

if __name__ == '__main__':
    unittest.main()
