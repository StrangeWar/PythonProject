st = str(input("Enter the string: "))
index = len(st)
Digits_count, Chars_count, Symbol_count = 0, 0, 0
Chars =""
Digits =""
Symbol =""

for i in range(index):
    if st[i].isalpha():                
        Chars = Chars+st[i]
        Chars_count+=1
    elif st[i].isdigit():
        Digits = Digits+st[i]
        Digits_count+=1
    else:
        Symbol = Symbol+st[i]
        Symbol_count+=1

print("Digits:",Digits,"|No. of Digits:",Digits_count)
print("Chars:",Chars," |No. of Chars:",Chars_count)
print("Symbol:",Symbol,"|No. of Symbol:",Symbol_count)
        