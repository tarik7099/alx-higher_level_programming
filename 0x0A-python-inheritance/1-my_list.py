#!/usr/bin/python3

"""Write a class MyList that inherits from list:"""


class MyList(list):
    """
    Prints the list in sorted (ascending) order.

    Args: self: The MyList object.

    Returns: Prints the sorted list.
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
