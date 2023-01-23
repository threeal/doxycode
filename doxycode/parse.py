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


def parse_doxygen_codes(comments: list[list[str]]) -> list[list[str]]:
    '''Parse Doxygen codes from multi line comments.'''
    raw_codes = []
    for comment in comments:
        is_code = False
        # parse raw code in each line
        for line in comment:
            if is_code:
                if line.find('@endcode') >= 0:
                    is_code = False
                raw_codes[-1].append(line)
                continue

            if line.find('@code') >= 0:
                is_code = True
                raw_codes.append([line])

    # filter raw codes
    codes = []
    for raw_code in raw_codes:
        # check if only contains begin and end line
        if len(raw_code) <= 2:
            continue

        raw_code = raw_code[1:-1]
        stripped_code = [ line.lstrip() for line in raw_code ]

        # check if all lines have a symbol prefix
        symbol = stripped_code[0][0]
        for idx, line in enumerate(stripped_code):
            # some has no symbol prefix, append raw instead
            if line[0] != symbol:
                break

            # all have a symbol prefix
            if idx == len(stripped_code) - 1:
                # replace all symbol prefix with a space
                raw_code = [ line.replace(symbol, ' ', 1) for line in raw_code ]

        codes.append(raw_code)

    return codes
