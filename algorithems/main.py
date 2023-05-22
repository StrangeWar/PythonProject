import random
from data import data
import timeit

dt = data


def linear_search(d, test):

    for i, item in enumerate(d):
        if item == test:
            return i
    return False


def binary_search(d, test):
    length = len(d)
    first = 0
    last = length-1

    while first <= last:
        middle = (first + last) // 2

        if d[middle] == test:
            return middle
        if test < d[middle]:
            last = middle - 1
        if test > d[middle]:
            first = middle + 1
    return False


key = random.randint(0, 100000000)
print("key:", key)
print(linear_search(data, key))
print(binary_search(data, key))

n = 5
result_linear = timeit.timeit(stmt='linear_search(data, key)', globals=globals(), number=n)
print("Execution time of linear search:", result_linear/n)

result_binary = timeit.timeit(stmt='binary_search(data, key)', globals=globals(), number=n)
print("Execution time of binary search:", result_binary/n)
