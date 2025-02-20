#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Data types


# In[2]:


#strings
print("123" + "456")


# In[3]:


#string like arrays
a = "hello"[1]
print(a)


# In[4]:


#using the negative indexing
b = "Godfather"[-4]
print(b)


# In[5]:


#integers
123  + 456


# In[6]:


#long integers
c = 123_456_789
print(c)


# In[7]:


#float 
d = 123.456
print(d)


# In[9]:


#boolean

f = 10>3
print(f)


# In[15]:


#type error and type checking 

a = type("!23")
b = type(123)
c = type(123_12_3123123123123)
d = type(123.42)
e = type(12>87)
print(a)
print(b)
print(c)
print(d)
print(e)


# In[16]:


#type conversions

print(int("123") + int("123"))


# In[17]:


print("Number of letters in your name: " + len(input("Enter your name: ")))


# In[23]:


length = len(input("Enter your name: "))
print("Number of letters in your name: " + str(length))


# In[2]:


#BMI Calculator

height = input("Enter your height in meters: ")
weight = input("Enter your weight in kilograms: ")

h = float(height)
w = float(weight)

bmi = w/h**2

print("Your bmi is: " + str(round(bmi,2)))


# In[3]:


#Mathematical operators 
#+=, -= , *= , /=

score = 0 
print(score)
score+=2
print(score)


# In[9]:


#F-string 
#It is a type of type convertor
a = 2
b = 1.23
c = "Hello"
d = True

#print(type(d))
print(f"hello the first one is: integer {a} " + f"The second one is float: {b} " +f"The third one is string: {c} " +f"The fourth one is a boolean: {d}")


# In[10]:


#Project TIP Calculator

print("Welcome to project tip Calculator!!")
bill = float(input("Enter the total bill: $"))
discount = float(input("How much discount do you want to get: "))
split = int(input("Enter the number of people to split the bill among: "))

bill_post_discount = bill-bill*discount/100
#print(bill_post_discount)
after_bill = round(bill_post_discount/split,2)
print(f"Each person would have to pay: {after_bill}$")

