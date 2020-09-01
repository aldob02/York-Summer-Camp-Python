import random

# alternative to min() function used in selection_sort()
# Example:
# >>> find_lowest([5,2,7,9,3])
# >>> 2
def find_lowest(lst):
    lowest = lst[0]
    for e in lst:
        if e < lowest:
            lowest = e
    return lowest

# Example:
# >>> selection_sort([5,2,7,9,3])
# >>> [2,3,5,7,9]
def selection_sort(lst):
    new_lst = []
    while len(lst) > 0:
        lowest = min(lst)
        lst.remove(lowest)
        new_lst.append(lowest)
    return new_lst

# Example:
# >>> rand_lst(4)
# >>> [5236, 8567, 2135]
def rand_lst(length):
    new_lst = []
    for i in range(length):
        new_lst.append(random.randint(-10000, 10000))
    return new_lst

# Example:
# >>> linear_search([5,2,7,9,3], 3)
# >>> True
# >>> linear_search([5,2,7,9,3], 8)
# >>> False
def linear_search(lst, target):
    for e in lst:
        if e == target:
            return True
    return False

# lst must be sorted
# Example:
# >>> binary_search([5,2,7,9,3], 3)
# >>> True
# >>> binary_search([5,2,7,9,3], 8)
# >>> False
def binary_search(lst, target):
    length = len(lst)
    median = lst[int(length/2)]
    if median == target:
        return True
    if median < target:
        return binary_search(lst[int(length/2)+1:], target)
    return binary_search(lst[:int(length/2)], target)

# Example:
# >>> merge_sort([5,2,7,9,3])
# >>> [2,3,5,7,9]
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = int(len(lst)/2)
    left = lst[:mid]
    right = lst[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

# Example:
# >>> merge([1,3,6], [2,7,9])
# >>> [1,2,3,6,7,9]
def merge(lst1, lst2):
    output = []
    while len(lst1) > 0 or len(lst2) > 0:
        if len(lst1) == 0:
            output = output + lst2
            lst2 = []
        elif len(lst2) == 0:
            output = output + lst1
            lst1 = []
        elif lst1[0] < lst2[0]:
            new_min = lst1[0]
            output.append(new_min)
            lst1.remove(new_min)
        else:
            new_min = lst2[0]
            output.append(new_min)
            lst2.remove(new_min)
    return output