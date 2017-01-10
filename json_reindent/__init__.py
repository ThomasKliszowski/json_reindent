import json
from json_reindent.utils import ordered_load


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
