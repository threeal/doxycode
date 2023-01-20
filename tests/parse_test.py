import pathlib
import unittest
from doxycode import parse_comments

class TestParse(unittest.TestCase):

  def setUp(self):
    self.root = pathlib.Path(__file__).parent.resolve()

  def test_parse_comments(self):
    with open(self.root / "sample/include/sample/sample.hpp", 'r') as file:
      comments = parse_comments(file)
      expected = ' namespace sample\n'
      self.assertEqual(comments, expected)

if __name__ == '__main__':
  unittest.main()
