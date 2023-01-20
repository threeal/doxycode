#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
  print('Usage: %s <filename>' % sys.argv[0])
  exit(1)

file = open(sys.argv[1], 'r')
for line in file.readlines():
  print(line, end='')
