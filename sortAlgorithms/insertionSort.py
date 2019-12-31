def _swap(lst, indexA, indexB):
    temp = lst[indexA]
    lst[indexA] = lst[indexB]
    lst[indexB] = temp
