def linear_search(list1, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list1):
        if item == key:
            return i
    return -1
    
list1 = ['vivek', 'sumit', 'aman', 'sobhit', 'ashutosh', 'prashant', 'abhijeet', 'ajeet', 'gopal', 'hanuman', 'mohit', 'ram', 'anita', 'ayush']
list1.sort()
print(list1)
print(linear_search(list1, 'mohit'))
