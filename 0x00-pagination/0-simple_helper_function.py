#!/usr/bin/env python3
'''module to find index of pagination'''


def index_range(page, page_size):
    '''function that returns start index & range of pagination'''
    sind = 0
    eind = 0

    if page != 1:
        sind = (page - 1) * page_size
    eind = sind + page_size

    return (sind, eind)
