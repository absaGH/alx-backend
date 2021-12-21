#!/usr/bin/env python3
'''module to create class BasicCache'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''inherits from BaseCaching and implements
       put and get methods
    '''

    def __init__(self):
        '''initialize BasicCache object'''
        super().__init__()
        self.keylst = []

    def put(self, key, item):
        '''implementation of mehtod of BaseCaching
           it add an item in the cache
        '''
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.keylst.append(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                indx = len(self.keylst) - 1
                removed = self.keylst[indx]
                self.cache_data.pop(self.keylst[indx])
                self.keylst.remove(self.keylst[indx])
                self.keylst.append(key)
                self.cache_data[key] = item
                print('DISCARD:', str(removed))
            else:
                self.cache_data[key] = item
                self.keylst.append(key)

    def get(self, key):
        '''implementation of method of BaseCaching
           it get an item by key
        '''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
