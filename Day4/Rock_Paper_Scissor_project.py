#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Randomisation and Lists


# In[9]:


random_num = random.randint(1,5)
print(random_num)


# In[8]:


import random


# In[13]:


#how to make your own module

#make a new file and import it using import module_name

#then use it as a function


# In[12]:


import my_module


# In[16]:


#random floating point numbers from 0 to 1 

print(random.random())


# In[18]:


import random

rand_num = random.randint(-9,6)

if rand_num%2 == 0:
    print("heads")
else:
    print("tails")

print(rand_num)


# In[21]:


#generating floating point numbers from 0 to 1 

print(random.random()*10)


# In[24]:


print(random.uniform(1,9))


# In[32]:


#to print heads or tails

ok = random.randint(0,1)

if ok == 1:
    print("Heads")
else:
    print("Tails")


# In[40]:


#Python Lists #Data structures

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

rand = random.randint(0,49)

print(states_of_america[rand])


# In[42]:


# we can change the values as well

states_of_america[4] = "Maharastra"

print(states_of_america[4])


# In[43]:


# we can add values asd well

states_of_america.append("Hellawood")
print(states_of_america)


# In[44]:


states_of_america.extend(["Hellawood","golwood","goa"])
print(states_of_america)


# In[57]:


# who will pay the bill
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random
rand = random.randint(0,4)

print(friends[rand])
print(random.choice(friends))


# In[2]:


#Indexing Errors
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(friends[9])


# In[3]:


#Nested Lists

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
# "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits,vegetables]

print(dirty_dozen)


# In[5]:


print(dirty_dozen[1])


# In[6]:


print(dirty_dozen[1][1])


# In[8]:


#Rock paper scissor

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

array = [rock,paper,scissors]
index = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

print(array[index])

import random
computer_choice = random.randint(0,2)

print("Computer chose: \n" + array[computer_choice])

if index == computer_choice:
    print("It's a draw")
elif index != computer_choice and index == 0:
    if computer_choice == 2:
        print("You win!")
    else:
        print("You lose")
elif index != computer_choice and index == 1:
    if computer_choice == 0:
        print("You win!")
    else:
        print("You lose")
elif index != computer_choice and index == 2:
    if computer_choice == 1:
        print("You win!")
    else:
        print("You lose")


# In[ ]:




