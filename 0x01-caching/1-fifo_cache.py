#!/usr/bin/env python3
"""
FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache is a caching system with FIFO eviction policy """

    def __init__(self):
        """ Initialize FIFOCache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_in_key = self.order.pop(0)
                del self.cache_data[first_in_key]
                print("DISCARD: {}".format(first_in_key))

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
