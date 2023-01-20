#!/usr/bin/env python3

'''Parse comments from a source code.'''

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
comments = parse_comments(file)
print(comments, end='')
