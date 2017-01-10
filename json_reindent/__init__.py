# Fix sublime text 2 / 3 compatibility
try:
    from json_reindent.utils import ordered_load
except ImportError:
    from .utils import ordered_load

import json


def parse_input(content, *args, **kwargs):
    return ordered_load(content, *args, **kwargs)


def format_output(data, indent=2, separators=[',', ': '], sort_keys=False, ensure_ascii=False):
    return json.dumps(
        data,
        indent=indent,
        separators=separators,
        sort_keys=sort_keys,
        ensure_ascii=ensure_ascii
    )
