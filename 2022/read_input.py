import pathlib


INPUT_DIR = pathlib.Path(__file__).parent / 'inputs'
DEFAULT_FORMAT_INPUT_FILES = 'day%s.txt'

def get_input_data(day: int, _format: str = DEFAULT_FORMAT_INPUT_FILES) -> str:
    """Read input data of given day from `inputs` directory"""
    filename = INPUT_DIR / (_format % day)
    with open(filename) as input_file:
        _input = input_file.read()
    return _input
