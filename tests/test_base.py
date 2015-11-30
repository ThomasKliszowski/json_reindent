from .utils import get_static_content, assert_static_test
from json_reindent import parse_input, format_output


def test_base():
    assert_static_test('base')


def test_unicode():
    assert_static_test('unicode')


def test_order():
    assert_static_test('order')


def test_no_collections():
    data = parse_input(get_static_content('order/test.json'), use_collections=False)
    output = format_output(data)
    assert output != get_static_content('order/result.json')


def test_trailing_comma():
    assert_static_test('trailing_comma')


def test_indent():
    data = parse_input(get_static_content('indent/test.json'), use_collections=False)
    output = format_output(data, indent=4)
    assert output == get_static_content('indent/result.json')
