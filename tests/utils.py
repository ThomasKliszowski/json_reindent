from os import path as op
from json_reindent import parse_input, format_output

CURRENT_DIR = op.dirname(__file__)


def get_static_content(filename):
    with open(op.join(CURRENT_DIR, 'static', filename), 'r') as fp:
        return fp.read().decode('utf-8')


def assert_static_test(static_test):
    data = parse_input(get_static_content('%s/test.json' % static_test))
    output = format_output(data)
    assert output == get_static_content('%s/result.json' % static_test)
