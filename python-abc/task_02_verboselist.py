#!/usr/bin/python3
"""
VerboseList
"""


class VerboseList(list):

    """
    Creating this with the built in list
    """

    def append(self, item):
        """
        print a message when append
        """
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, item):
        """
        print a message when extend
        """
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        """
        print a message when remove
        """
        super().remove(item)
        print("Removed [{}] from the list".format(item))

    def pop(self, index=-1):
        """
        print a message when pop
        """
        removed_item = super().pop(index)
        print("Popped [{}] from the list".format(removed_item))
        return removed_item
