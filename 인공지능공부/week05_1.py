def countsort(lst):
    return sorted([(x, lst.count(x)) for x in set(lst)])

numbers = [1, 2, 2, 3, 4, 3, 2, 5]
print(countsort(numbers))
