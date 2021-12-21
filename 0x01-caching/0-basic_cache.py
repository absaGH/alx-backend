#!/usr/bin/env python3
'''module to create class BasicCache'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''inherits from BaseCaching and implements
       put and get methods
    '''

    def __init__(self):
        '''initialize BasicCache object'''
        super().__init__()

    def put(self, key, item):
        '''implementation of mehtod of BaseCaching
           it add an item in the cache
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''implementation of method of BaseCaching
           it get an item by key
        '''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
