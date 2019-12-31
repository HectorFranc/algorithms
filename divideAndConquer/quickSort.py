def swap(lst, indexA, indexB):
    lst[indexA], lst[indexB] = lst[indexB], lst[indexA]


def quickSort(lst, min_inclusive=0, max_inclusive=None):
    '''
    Quick sort algorithm.

    Parameters:

    - lst: list

        List to be sorted.

    - min_inclusive: int, optional, default: 0

        Minimum index of sub-list to be sorted.

    - max_inclusive: int, optional, default: len(lst) - 1

        Maximum index of sub-list to be sorted.
    '''
    if max_inclusive is None:
        # Max inclusive will be the pivot
        max_inclusive = len(lst) - 1

    # If not in base case: list has not 0 or 1 element (are not already ordered)
    if min_inclusive < max_inclusive:

        # Group separator
        index_min_of_group_bigger = min_inclusive
        # Partition
        pivot_value = lst[max_inclusive]

        for index_min_of_group_unknown in range(min_inclusive, max_inclusive):
            if lst[index_min_of_group_unknown] <= pivot_value:
                swap(lst, index_min_of_group_bigger, index_min_of_group_unknown)
                index_min_of_group_bigger += 1

        swap(lst, index_min_of_group_bigger, max_inclusive)

        # Recursion
        quickSort(lst, min_inclusive, index_min_of_group_bigger - 1)
        quickSort(lst, index_min_of_group_bigger + 1, max_inclusive)
