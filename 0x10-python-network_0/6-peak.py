#!/usr/bin/python3
""" find peak"""
def find_peak(list_of_integers):
    """
    find peak
    """
    if not list_of_integers:
        return None
    
    low, high = 0, len(list_of_integers) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        
        # If the left neighbor is greater, search in the left half
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            high = mid - 1
        
        # Otherwise, search in the right half
        else:
            low = mid + 1
    
    return None
