# Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
list1 = [5, 10, 15, 20, 25, 50, 20]
for x in list1:
    if x==20:
        list1[list1.index(x)]=200
        break
    
print(list1)        