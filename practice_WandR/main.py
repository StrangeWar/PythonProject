# with open(r'/Users/Vivek Sharma/Desktop/vivek.txt', mode='a') as data:
#     content = data.write('/nThis is a writing test.')

with open("../../../desktop/vivek.txt") as data:
    content2 = data.read()
    print(content2)