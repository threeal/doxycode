'''Provide functions for parsing comments from a source code.'''

def get_next_char(line: str, index: int) -> str:
    '''Get the next character of an index from a string.'''
    return line[index + 1] if index + 1 < len(line) else ''


def get_prev_char(line: str, index: int) -> str:
    '''Get the previous character of an index from a string.'''
    return line[index - 1] if index > 0 else ''


def parse_comments(file) -> list[str]:
    '''Parse comments from a file.'''
    comments = []
    for line in file.readlines():
        # find the first occurrence of a forward slash
        first = line.find('/')
        if first < 0:
            continue

        # the forward slash is a part of a single-line comment
        char = get_next_char(line, first)
        if char == '/':
            comments.append(line[first+2:])
        elif char == '*':
            line = line[first+2:]
            second = line.find('/')
            if second >= 0 and get_prev_char(line, second) == '*':
                comments.append(line[:second-1])

    return comments
