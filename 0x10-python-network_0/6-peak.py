#!/usr/bin/python3
"""
finds the peak in a list of unsorted int
"""


def find_peak(list_of_integers):
    """ Returns a peak of unsort int using binary search """
    if not list_of_integers:
        return None

    start = 0
    end = len(list_of_integers) - 1

    while start < end:
        mid = (start + end) // 2

        if list_of_integers[mid] > list_of_integers[mid - 1] and \
           list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            start = mid + 1
        else:
            end = mid - 1

    return list_of_integers[start]
