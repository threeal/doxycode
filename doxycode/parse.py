'''Provide functions for parsing contents of a source code.'''

def get_next_char(line: str, index: int) -> str:
    '''Get the next character of an index from a string.'''
    return line[index + 1] if index + 1 < len(line) else ''


def get_prev_char(line: str, index: int) -> str:
    '''Get the previous character of an index from a string.'''
    return line[index - 1] if index > 0 else ''


def parse_doxygen_comments(file) -> list[str]:
    '''Parse Doxygen comments from a file.'''
    comments = []
    is_multiline = False
    for line in file.readlines():
        # find the first occurrence of a forward slash
        index = line.find('/')
        if index < 0:
            # append all line if still in the multiline comment
            if is_multiline:
                comments[-1] += line
            continue

        if is_multiline:
            # check if it's the end of the multiline comment
            if get_prev_char(line, index) == '*':
                comments[-1] += line[:index-1]
                is_multiline = False
            else:
                # append all line if it's not the end
                comments[-1] += line
            continue

        # check if it's the start of the multiline comment
        if get_next_char(line, index) == '*':
            if get_next_char(line, index + 1) == '*':
                is_multiline = True
                comments.append(line[index+3:])

    return comments
