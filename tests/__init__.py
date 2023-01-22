'''Test functions for parsing codes from a Doxygen project.'''

import pathlib
import sys

PROJECT_PATH = pathlib.Path(__file__).parent.parent.resolve()
sys.path.append(PROJECT_PATH)
