'''Provide functions for parsing contents of a source code.'''

def get_next_char(line: str, index: int) -> str:
    '''Get the next character of an index from a string.'''
    return line[index + 1] if index + 1 < len(line) else ''


def get_prev_char(line: str, index: int) -> str:
    '''Get the previous character of an index from a string.'''
    return line[index - 1] if index > 0 else ''


def parse_multiline_comments(file) -> list[list[str]]:
    '''Parse multi line comments from a file.'''
    comments = []
    is_multiline = False
    for line in file.readlines():
        # Clear a new line from the line
        if line[-1] == '\n':
            line = line[:-1]

        # find the first occurrence of a forward slash
        index = line.find('/')
        if index < 0:
            # append all line if still in the multi line comment
            if is_multiline:
                comments[-1].append(line)
            continue

        if is_multiline:
            comments[-1].append(line)
            # check if it's the end of the multi line comment
            if get_prev_char(line, index) == '*':
                is_multiline = False
            continue

        # check if it's the start of the multi line comment
        if get_next_char(line, index) == '*':
            subline = line
            subindex = index
            while True:
                subline = subline[subindex+1:]
                subindex = subline.find('/')
                if subindex < 0:
                    is_multiline = True
                    comments.append([line])
                    break

                # skip if a single line comment
                if get_prev_char(subline, subindex) == '*':
                    break

    return comments
