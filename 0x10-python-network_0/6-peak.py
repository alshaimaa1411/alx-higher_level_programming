def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using a binary search inspired approach.
    
    Args:
    - list_of_integers: A list of unsorted integers
    
    Returns:
    - A peak element if found, None if the list is empty
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


print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

