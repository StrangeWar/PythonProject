# Initialize dictionary with default values

# method 1
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dictsalary = {key:defaults for key in employees}
print(dictsalary)

# method 2

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["Kelly"])