s1 = str(input("Enter the 1st String: "))
s2 = str(input("Enter the 2st String: "))
index = int(len(s1))
mi = int(index/2)
s3 = s1[:mi]+s2+s1[mi:]
print(s3)
