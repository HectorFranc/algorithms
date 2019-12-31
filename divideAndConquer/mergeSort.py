def merge(lst, low, high, mid_high):
    # Temporal copies of arrays
    temp_low = lst[low:mid_high]
    temp_high = lst[mid_high:high + 1]

    # Min index not checked of every temp array
    index_temp_low, index_temp_high = 0, 0

    # Index for be over-written in lst
    index_lst = low

    # Actual index of lst has min of temp lists
    while index_temp_low < len(temp_low) and index_temp_high < len(temp_high):

        if temp_low[index_temp_low] <= temp_high[index_temp_high]:
            lst[index_lst] = temp_low[index_temp_low]
            index_temp_low += 1
        else:
            lst[index_lst] = temp_high[index_temp_high]
            index_temp_high += 1

        index_lst += 1

    # When a temp list is all checked the other elements are already ordered
    while index_temp_low < len(temp_low):
        lst[index_lst] = temp_low[index_temp_low]
        index_lst += 1
        index_temp_low += 1

    while index_temp_high < len(temp_high):
        lst[index_lst] = temp_high[index_temp_high]
        index_lst += 1
        index_temp_high += 1


def merge_sort(lst, min_inclusive=0, max_inclusive=None):
    '''
    Merge sort algorithm.

    Parameters:

    - lst: list

        List to be sorted.

    - min_inclusive: int, optional, default: 0

        Minimum index of sub-list to be sorted.

    - max_inclusive: int, optional, default: len(lst) - 1

        Maximum index of sub-list to be sorted.
    '''
    if max_inclusive is None:
        max_inclusive = len(lst) - 1

    # If not in base case: list has not 0 or 1 element (are not already ordered)
    if min_inclusive < max_inclusive:
        merge_sort(lst, min_inclusive, (min_inclusive + max_inclusive) // 2)
        merge_sort(lst, (min_inclusive + max_inclusive) // 2 + 1, max_inclusive)
        merge(lst, min_inclusive, max_inclusive, (min_inclusive + max_inclusive) // 2 + 1)
