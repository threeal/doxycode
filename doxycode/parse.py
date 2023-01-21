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
    is_multiline = False
    for line in file.readlines():
        # find the first occurrence of a forward slash
        first = line.find('/')
        if first < 0:
            if is_multiline:
                comments[-1] += line
            continue

        if is_multiline:
            char = get_prev_char(line, first)
            if char == '*':
                comments[-1] += line[:first-1]
                is_multiline = False
            else:
                comments[-1] += line
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
            else:
                comments.append(line)
                is_multiline = True

    return comments
