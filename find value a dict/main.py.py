# Write a Python program to check if value 200 exists in the following dictionary.


value = eval(input("Enter the value: "))
sample_dict = {'a': 100, 'b': 200, 'c': 300}

values = sample_dict.values()
if value in values:
    print("{} is present  in the dictionary".format(value))
else:
    print("{} is not present  in the dictionary".format(value))