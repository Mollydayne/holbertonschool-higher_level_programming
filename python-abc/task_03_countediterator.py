#!/usr/bin/python3
"""
CountedIterator
"""
from abc import ABC, abstractmethod



class CountedIterator:

    """
    keep track of the number of items that have been iterated over
    """

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        return self
