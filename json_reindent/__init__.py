import yaml
import json
import logging
from .utils import ordered_load

logger = logging.getLogger(__name__)


def parse_input(content, *args, **kwargs):
    return ordered_load(content, yaml.SafeLoader, *args, **kwargs)


def format_output(data, indent=2, separators=[',', ': '], sort_keys=False, ensure_ascii=False):
    return json.dumps(
        data,
        indent=indent,
        separators=separators,
        sort_keys=sort_keys,
        ensure_ascii=ensure_ascii
    )
