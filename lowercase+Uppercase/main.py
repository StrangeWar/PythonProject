s1 = str(input("Enter the String: "))
index = len(s1)
lower = ""
upper = ""

for i in range(index):
    if s1[i].islower():
        lower = lower+s1[i]
    else :
        upper = upper+s1[i]
    
    
print(lower+upper)    
    