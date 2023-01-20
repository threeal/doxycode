'''Provide functions for parsing comments from a source code.'''

def get_next(line: str, index: int) -> str:
    '''Get the next character of an index from a string.'''
    return line[index + 1] if index + 1 < len(line) else ''


def parse_comments(file) -> str:
    '''Parse comments from a file.'''
    out = ''
    for line in file.readlines():
        # find the first occurrence of a forward slash
        index = line.find('/')
        if index < 0:
            continue

        # the forward slash is a part of a single-line comment
        if get_next(line, index) == '/':
            out += line[index+2:]

    return out
