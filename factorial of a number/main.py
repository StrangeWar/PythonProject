num = int(input("Enter the Numer: "))
factorial=1 
if num < 0 :
    print('factorial of negetive number is not possible')
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("factorial of ",num," is =",str(factorial))
    