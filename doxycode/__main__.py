#!/usr/bin/env python3

'''Parse Doxygen codes from a file.'''

import os
import sys

from .parse import parse_multiline_comments, parse_doxygen_codes

if len(sys.argv) < 2:
    EXE = 'doxycode.py'
    if len(sys.argv) > 0:
        EXE = os.path.basename(sys.argv[0])
    print(f'Usage: {EXE} <filename>')
    sys.exit(1)

with open(sys.argv[1], 'r', encoding="utf-8") as file:
    comments = parse_multiline_comments(file)
    codes = parse_doxygen_codes(comments)
    for i, code in enumerate(codes):
        if i > 0:
            print()
        for line in code:
            print(line)
