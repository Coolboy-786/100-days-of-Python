#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Day5 loops , Range and code Blocks


# In[2]:


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]


# In[3]:


for states in states_of_america:
    print(states)


# In[10]:


i=1
for states in states_of_america:
    print(str(i) +") "+ states)
    i+=1


# In[11]:


student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))


# In[12]:


print(sum(student_scores))


# In[14]:


#sum function
sum = 0
for score in student_scores:
    sum+=score
print(sum)


# In[15]:


#max function
max=0 

for scores in student_scores:
    if max<scores:
        max=scores
print(max)


# In[18]:


#min function
min = student_scores[0] 

for scores in student_scores:
    if min>scores:
        min=scores
print(min)


# In[23]:


#Avg function

avg = 0 
sum = 0 
for scores in student_scores:
    sum+=scores
avg=sum/len(student_scores)
print(avg)
    


# In[24]:


#Range

for numbers in range(1,11):
    print(numbers)


# In[26]:


#Range(a: first,b: last,c: gaps(by default is zero))

for number in range(1,100,7):
    print(number-1)


# In[29]:


#sum of numbers from 1 to 100
sum=0
for num in range(1,101):
    sum+=num
print(sum)


# In[32]:


for num in range(1,101):
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num%3 == 0:
        print("Fizz")
    elif num%5 == 0:
        print("Buzz")
    else:
        print(num)


# In[33]:


import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Generate password components
chosen_letters = [random.choice(letters) for _ in range(nr_letters)]
chosen_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
chosen_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

# Easy password (ordered)
easy_password = "".join(chosen_letters + chosen_symbols + chosen_numbers)
print("Your easy password is:", easy_password)

# Hard password (shuffled)
password_list = chosen_letters + chosen_symbols + chosen_numbers
random.shuffle(password_list)  # Shuffle in place
hard_password = "".join(password_list)

print("Your hard password is:", hard_password)


# In[ ]:


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
print("".join(hard_password))


# In[35]:


#Angela try

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level
# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(password)

# Hard level
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")


# In[ ]:




