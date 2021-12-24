#!/usr/bin/env python3
'''module to create class MRUCache'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''inherits from BaseCaching and implements
       MRU caching policy
    '''

    def __init__(self):
        '''initialize MRUCache object'''
        super().__init__()
        self.keydict = {}

    def put(self, key, item):
        '''implementation of mehtod of BaseCaching
           it add an item in the cache
        '''
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                MRUkey = max(self.keydict, key=self.keydict.get)
                self.keydict[key] = self.keydict[MRUkey] + 1
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = max(self.keydict, key=self.keydict.get)
                removed_val = self.keydict[removed]
                self.cache_data.pop(removed)
                self.keydict.pop(removed)
                if not bool(self.keydict):
                    self.keydict[key] = removed_val + 1
                else:
                    MRUkey = max(self.keydict, key=self.keydict.get)
                    self.keydict[key] = self.keydict[MRUkey] + 1
                self.cache_data[key] = item
                print('DISCARD:', str(removed))
            else:
                self.cache_data[key] = item
                has_item = bool(self.keydict)
                if not has_item:
                    self.keydict[key] = 0
                else:
                    MRUkey = max(self.keydict, key=self.keydict.get)
                    self.keydict[key] = self.keydict[MRUkey] + 1

    def get(self, key):
        '''implementation of method of BaseCaching
           it get an item by key
        '''
        if key is not None and key in self.cache_data:
            MRUkey = max(self.keydict, key=self.keydict.get)
            self.keydict[key] = self.keydict[MRUkey] + 1
            return self.cache_data[key]
        else:
            return None
