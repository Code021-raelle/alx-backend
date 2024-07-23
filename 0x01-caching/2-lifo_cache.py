#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache is a caching system with LIFO eviction """

    def __init__(self):
        """ Initialize LIFOCache """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    if self.last_key is not None:
                        print("DISCARD: {}".format(self.last_key))
                        del self.cache_data[self.last_key]
                self.cache_data[key] = item
                self.last_key = key

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
