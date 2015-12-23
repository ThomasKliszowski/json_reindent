from .utils import get_static_content, assert_static_test
from json_reindent import parse_input, format_output
import json


def test_base():
    assert_static_test('base')


def test_unicode():
    assert_static_test('unicode')


def test_order():
    import collections
    if hasattr(collections, 'OrderedDict'):
        assert_static_test('order')
    else:
        assert_static_test('order', False)


def test_trailing_comma():
    assert_static_test('trailing_comma')


def test_indent():
    data = parse_input(get_static_content('indent/test.json'))
    output = format_output(data, indent=4)
    assert output == get_static_content('indent/result.json')


def test_no_collections():
    data = parse_input(get_static_content('base/test.json'), use_collections=False)
    output = format_output(data)
    assert json.loads(output) == json.loads(get_static_content('base/result.json'))


def test_fail_yaml():
    data = parse_input(get_static_content('fail_yaml/test.json'))
    output = format_output(data)
    assert json.loads(output) == json.loads(get_static_content('fail_yaml/result.json'))
