def _swap(lst, indexA, indexB):
    temp = lst[indexA]
    lst[indexA] = lst[indexB]
    lst[indexB] = temp


def insertion_sort(lst):
    for i in range(1, len(lst)):
        tmp = lst[i]
        actual_index = i - 1
        while str(tmp) < str(lst[actual_index]) and actual_index >= 0:
            lst[actual_index + 1] = lst[actual_index]
            actual_index -= 1
        lst[actual_index + 1] = tmp
