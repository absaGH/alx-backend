#!/usr/bin/env python3
'''module to create class LRUCache'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''inherits from BaseCaching and implements
       LRU caching policy
    '''

    def __init__(self):
        '''initialize LRUCache object'''
        super().__init__()
        self.keydict = {}

    def put(self, key, item):
        '''implementation of mehtod of BaseCaching
           it add an item in the cache
        '''
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.keydict[key] = self.keydict[max(
                    self.keydict, key=self.keydict.get)] + 1
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = min(self.keydict, key=self.keydict.get)
                removed_val = self.keydict[removed]
                self.cache_data.pop(removed)
                self.keydict.pop(removed)
                if not bool(self.keydict):
                    self.keydict[key] = removed_val + 1
                else:
                    self.keydict[key] = self.keydict[max(
                        self.keydict, key=self.keydict.get)] + 1
                self.cache_data[key] = item
                print('DISCARD:', str(removed))
            else:
                self.cache_data[key] = item
                has_item = bool(self.keydict)
                if not has_item:
                    self.keydict[key] = 0
                else:
                    self.keydict[key] = self.keydict[max(
                        self.keydict, key=self.keydict.get)] + 1

    def get(self, key):
        '''implementation of method of BaseCaching
           it get an item by key
        '''
        if key is not None and key in self.cache_data:
            self.keydict[key] = self.keydict[max(
                self.keydict, key=self.keydict.get)] + 1
            return self.cache_data[key]
        else:
            return None
