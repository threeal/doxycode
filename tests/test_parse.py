'''Test functions for parsing contents of a source code.'''

import json
import pathlib
import unittest
from doxycode import parse_multiline_comments


class TestParse(unittest.TestCase):
    '''The unit testing class.'''


    def setUp(self):
        self.root = pathlib.Path(__file__).parent.resolve()
        self.source_dir = self.root / 'sample/include'

        self.test_cases = ['sample/sample.hpp']

        # Load expectations data from JSON files
        self.expectations_map = {}
        for test_case in self.test_cases:
            path = self.root / 'sample/expectation' / (test_case + '.json')
            with open(path, 'r', encoding='utf-8') as file:
                txt = file.read()
                self.expectations_map[test_case] = json.loads(txt)


    def test_parse_multiline_comments(self):
        '''Test a function for parsing multi line comments from a file.'''

        for test_case in self.test_cases:
            expectations = self.expectations_map[test_case]
            with open(self.source_dir / test_case, 'r', encoding='utf-8') as file:
                comments = parse_multiline_comments(file)
                for comment, expectation in zip(comments, expectations):
                    self.assertListEqual(comment, expectation)
                self.assertEqual(len(comments), len(expectations))


if __name__ == '__main__':
    unittest.main()
