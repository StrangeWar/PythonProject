#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
len_letters = len(letters)
len_symbols = len(symbols)
len_numbers = len(numbers)

password =[]
for i in range(nr_letters):
  password.insert(i, letters[random.randint(0,len_letters-1)])
  
for j in range(nr_symbols):
  password.insert(random.randint(0,len(password)-1), symbols[random.randint(0,len_symbols-1)])

for k in range(nr_numbers):
  password.insert(random.randint(0,len(password)-1), numbers[random.randint(0,len_numbers-1)])

final_password = "".join(password)

print(f"Here is your password: {final_password}")

