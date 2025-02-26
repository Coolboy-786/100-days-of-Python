#My try

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

i=0
j=0
k=0
choice1 = ""
for let in letters:
    i+=1
    if i<=nr_letters:
        let = random.choice(letters)
        #print(let)
        choice1+=let
for sym in symbols:
    j+=1
    if j<=nr_symbols:
        sym = random.choice(symbols)
        #print(sym)
        choice1+=sym
for num in numbers:
    k+=1
    if k<=nr_symbols:
        num = random.choice(numbers)
        #print(num)
        choice1+=num

print("Your easy password is: " + choice1)

# print(password)
hard_password = random.sample(choice1,len(choice1))
#print("Your hard password is: " + random.shuflehard_password)
print("Your hard password is: ")
print("".join(hard_password))