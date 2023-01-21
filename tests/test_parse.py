'''Test functions for parsing contents of a source code.'''

import json
import pathlib
import unittest
from doxycode import parse_multiline_comments


class TestParse(unittest.TestCase):
    '''The unit testing class.'''


    def setUp(self):
        root = pathlib.Path(__file__).parent.resolve()
        raw_test_cases = ['sample/sample.hpp']

        self.test_cases = []
        for test_case in raw_test_cases:
            self.test_cases.append(root / 'sample/include' / test_case)

        # Load expectations data from JSON files
        self.expectations_map = {}
        for raw_test_case, test_case in zip(raw_test_cases, self.test_cases):
            path = root / 'sample/expectation' / (raw_test_case + '.json')
            with open(path, 'r', encoding='utf-8') as file:
                txt = file.read()
                self.expectations_map[test_case] = json.loads(txt)


    def test_parse_multiline_comments(self):
        '''Test a function for parsing multi line comments from a file.'''

        for test_case in self.test_cases:
            expectations = self.expectations_map[test_case]
            with open(test_case, 'r', encoding='utf-8') as file:
                comments = parse_multiline_comments(file)
                for comment, expectation in zip(comments, expectations):
                    self.assertListEqual(comment, expectation)
                self.assertEqual(len(comments), len(expectations))


if __name__ == '__main__':
    unittest.main()
