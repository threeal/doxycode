'''Test functions for parsing contents of a source code.'''

import json
import pathlib
import unittest
from doxycode import parse_doxygen_comments

class TestParse(unittest.TestCase):
    '''The unit testing class.'''

    def setUp(self):
        self.root = pathlib.Path(__file__).parent.resolve()
        self.source_dir = self.root / 'sample/include'
        self.expectation_dir = self.root / 'sample/expectation'

    def test_parse_doxygen_comments(self):
        '''Test a function for parsing Doxygen comments from a file.'''
        test_cases = ['sample/sample.hpp']
        for test_case in test_cases:
            with open(self.source_dir / test_case, 'r', encoding='utf-8') as file:
                comments = parse_doxygen_comments(file)
                expectation_path = self.expectation_dir / (test_case + '.json')
                with open(expectation_path, 'r', encoding='utf-8') as file:
                    file_txt = file.read()
                    expectations = json.loads(file_txt)
                    for comment, expectation in zip(comments, expectations):
                        self.assertListEqual(comment, expectation)
                    self.assertEqual(len(comments), len(expectations))

if __name__ == '__main__':
    unittest.main()
