import yaml
import collections


def ordered_load(stream, Loader=yaml.Loader, use_collections=True):
    if use_collections and hasattr(collections, 'OrderedDict'):
        object_pairs_hook = collections.OrderedDict
    else:
        object_pairs_hook = dict

    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)

    return yaml.load(stream, OrderedLoader)
