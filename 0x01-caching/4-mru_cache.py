#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCache is a caching system with MRU eviction policy """

    def __init__(self):
        """ Initialize MRYCache """
        super().__init__()
        self.cache_data = OrderedDict()
        
    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
