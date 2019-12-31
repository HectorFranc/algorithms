def _swap(lst, indexA, indexB):
    temp = lst[indexA]
    lst[indexA] = lst[indexB]
    lst[indexB] = temp


def bubble_sort(lst):
    actual_max_index = len(lst) - 1
    while actual_max_index > 0:
        for i in range(0, actual_max_index):
            if lst[i] > lst[i + 1]:
                _swap(lst, i, i + 1)
        actual_max_index -= 1
    return lst
