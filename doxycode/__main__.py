#!/usr/bin/env python3

'''Parse Doxygen comments from a file.'''

import os
import sys

from .parse import parse_doxygen_comments

if len(sys.argv) < 2:
    EXE = 'doxycode.py'
    if len(sys.argv) > 0:
        EXE = os.path.basename(sys.argv[0])
    print(f'Usage: {EXE} <filename>')
    sys.exit(1)

with open(sys.argv[1], 'r', encoding="utf-8") as file:
    comments = parse_doxygen_comments(file)
    for comment in comments:
        for line in comment:
            print(line, end='')
