#!/usr/bin/env python3

import os
import sys

from .parse import parse_comments

if len(sys.argv) < 2:
  executable = 'doxycode.py'
  if len(sys.argv) > 0:
    executable = os.path.basename(sys.argv[0])
  print('Usage: %s <filename>' % executable)
  exit(1)

file = open(sys.argv[1], 'r')
parse_comments(file)
