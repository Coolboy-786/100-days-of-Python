#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Day3 Conditionals,logical operators, Code Blocks and scope


# In[3]:


print("Welcome to the Rollarcoster")


# In[6]:


#height = int(input("Enter your height in cms: "))


# In[5]:


if height>=120:
    print("You can ride the rollarcoster")
else:
    print("Sorry, You have to grow taller to ride the rollarcoster ")


# In[8]:


height = int(input("Enter your height in cms: "))
if height>=120:
    print("You can ride the rollarcoster")
else:
    print("Sorry, You have to grow taller to ride the rollarcoster ")


# In[9]:


#Modulo operator (%)
10%3


# In[12]:


a = int(input("Enter the dividend: "))
b = int(input("Enter the divisor: "))
c = int(a/b)
d = a%b

print("The Quotient is "+str(c)+" and the remainder is "+ str(d))


# In[14]:


#Even Odd checker
num = int(input("Enter the number: "))
if(num%2 == 0):
    print(str(num)+ " is even")
else:
    print(str(num)+ " is odd")


# In[15]:


height1 = int(input("Enter your height in cms: "))
if height1>=120:
    print("You can ride the rollarcoster")
    age = int(input("Enter your age: "))
    if age>18:
        print("You have to pay $12")
    elif age>=12 and age<=18:
        print("You have to pay $7")
    elif age<12:
        print("You have to pay $5")
else:
    print("Sorry, You have to grow taller to ride the rollarcoster ")


# In[17]:


#New BMI Calculator
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi<18.5:
    print("underweight")
elif bmi>=18.5 and bmi<25:
    print("normal weight")
else:
    print("overweight")


# In[4]:


height1 = int(input("Enter your height in cms: "))
bill=0
if height1>=120:
    print("You can ride the rollarcoster")
    age = int(input("Enter your age: "))
    if age>18:
        bill=12
        print("You have to pay $12")
    elif age>=12 and age<=18:
        bill=7
        print("You have to pay $7")
    elif age<12:
        bill=5
        print("You have to pay $5")
    photo = input("Do you want to buy a photo if yes then y else n: ")
    if photo == "y":
        bill+=3
    print(f"You final bill to pay ${bill}")
else:
    print("Sorry, You have to grow taller to ride the rollarcoster ")


# In[5]:


#Pizza order Practice
print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if size == "S":
    bill+=15
    if pepperoni == "y":
        bill += 2
elif size == "M":
    bill+=20
    if pepperoni == "y":
        bill += 3
elif size == "L":
    bill+=25
    if pepperoni == "y":
        bill += 3
if extra_cheese == "Y":
    bill+=1

print(f"Your final bill is {bill}")


# In[6]:


print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if size == "S":
    bill+=15
elif size == "M":
    bill+=20
elif size == "L":
    bill+=25

if pepperoni == "y":
    if size == "S":
    bill+=2
    else:
    bill+=3

if extra_cheese == "Y":
    bill+=1
    
print(f"Your final bill is {bill}")


# In[8]:


print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if size == "S":
    bill+=15
elif size == "M":
    bill+=20
elif size == "L":
    bill+=25

if pepperoni == "y":
    if size == "S":
        bill+=2
    else:
        bill +=3
    

if extra_cheese == "Y":
    bill+=1

print(f"Your final bill is ${bill}")


# In[9]:


True and True


# In[10]:


True and False


# In[11]:


False and False


# In[ ]:


height1 = int(input("Enter your height in cms: "))
bill=0
if height1>=120:
    print("You can ride the rollarcoster")
    age = int(input("Enter your age: "))
    if age>18 and age<45:
        bill=12
        print("You have to pay $12")
    elif age>=12 and age<=18:
        bill=7
        print("You have to pay $7")
    elif age<12:
        bill=5
        print("You have to pay $5")
    elif age>=45 and age<=55:
        bill=0
    photo = input("Do you want to buy a photo if yes then y else n: ")
    if photo == "y":
        bill+=3
    print(f"You final bill to pay ${bill}")
else:
    print("Sorry, You have to grow taller to ride the rollarcoster ")


# In[14]:


height1 = int(input("Enter your height in cms: "))
bill=0
if height1>=120:
    print("You can ride the rollarcoster")
    age = int(input("Enter your age: "))
    if age>18 and age<45:
        bill=12
        print("You have to pay $12")
    elif age>=12 and age<=18:
        bill=7
        print("You have to pay $7")
    elif age<12:
        bill=5
        print("You have to pay $5")
    elif age>=45 and age<=55:
        bill=0
    photo = input("Do you want to buy a photo if yes then y else n: ")
    if photo == "y":
        bill+=3
    print(f"You final bill to pay ${bill}")
else:
    print("Sorry, You have to grow taller to ride the rollarcoster ")


# In[15]:


print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


# In[16]:


print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go?")
road = input("Type left or right: ")

if road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake = input("Type wait to wait for a boat. Type swim to swim across: ")
    if lake == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door = input("One red, one yellow and one blue. Which colour do you choose: ")
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")
        elif door == "yellow":
            print("You win!!!")
        else:
            print("Game over :|")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")


# In[ ]:




