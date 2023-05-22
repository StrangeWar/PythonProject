def binary_search(list1, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list1) - 1
    while left <= right:
        middle = (left + right) // 2
        
        if list1[middle] == key:
            return middle
        if list1[middle] > key:
            right = middle - 1
        if list1[middle] < key:
            left = middle + 1
    return -1
    
list1 = ['vivek', 'sumit', 'aman', 'sobhit', 'ashutosh', 'prashant', 'abhijeet', 'ajeet', 'gopal', 'hanuman', 'mohit', 'ram', 'anita', 'ayush']
list1.sort()
print(list1)
print(binary_search(list1, 'mohit'))
