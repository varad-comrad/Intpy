def quicksort(list):
    if len(list) <= 1:
        return list

    pivot = list[0]
    equal = [x for x in list if x == pivot]
    greater = [x for x in list if x > pivot]
    lesser = [x for x in list if x < pivot]

    return quicksort(lesser) + equal + quicksort(greater)
