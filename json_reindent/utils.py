import json
import yaml
import collections
import logging

logger = logging.getLogger(__name__)


def ordered_load(stream, use_collections=True):
    if use_collections and hasattr(collections, 'OrderedDict'):
        object_pairs_hook = collections.OrderedDict
    else:
        object_pairs_hook = dict

    try:
        return yaml_ordered_load(stream, object_pairs_hook)
    except Exception as e:
        logger.error(e, exc_info=True)

        return json_ordered_load(stream, object_pairs_hook)


def json_ordered_load(stream, object_pairs_hook):
    params = {
        's': stream,
        'strict': False,
        'object_pairs_hook': object_pairs_hook
    }

    try:
        return json.loads(**params)
    except TypeError:
        # Fix python 2.6
        del params['object_pairs_hook']
        return json.loads(**params)


def yaml_ordered_load(stream, object_pairs_hook, Loader=yaml.Loader):
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)

    return yaml.load(stream, OrderedLoader)
