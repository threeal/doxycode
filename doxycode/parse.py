def parse_comments(file):
  for line in file.readlines():
    # find the first occurrence of a forward slash
    index = line.find('/')
    if index < 0 or index >= len(line) - 1:
      continue

    # the forward slash is a part of a single-line comment
    if line[index + 1] == '/':
      print('%s' % line[index+2:], end='')
