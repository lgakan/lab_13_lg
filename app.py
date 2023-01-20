
def bubblesort(toSort):
    n = len(toSort)
    toSort = toSort[:]
    number_of_compare = 0
    while n > 1:
        is_sorted = True
        for i in range(1, n):
            number_of_compare += 1
            if toSort[i - 1] > toSort[i]:
                [toSort[i - 1], toSort[i]] = [toSort[i], toSort[i - 1]]
                is_sorted = False
        if is_sorted:
            break
        n = n - 1

    return toSort, number_of_compare
