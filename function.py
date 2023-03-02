# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 21:23:15 2023

@author: PADMESH
"""



# ---------------------------------------------------
#Functions
#----------------------------------------------------
#example1
def test(s1):
   "demo of function"
   print(s1)
 

test("hello world")
#
def test(s1):
   "demo of function"
   return s1

test("hello world")


import math

#example2 to find the sqrt of a number
def test(n):
   "demo of function"
   print(math.sqrt(n))
   

test(25)

#Function Ploymorphism

def product(x, y) : 
    return x * y
print(product(4, 9)) 
# function returns 36
product(10, 20)
print(product('hello', 2))  

def product(x, y,z) : 
    return x * y * z

product(10, 20,30)

#to find the factorial of an integer with recurssion
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1 or x==0:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value for a different result
num = 5

# to take input from the user
# num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)


a = 0
b = 1
n=5
i=1
a
b
while i < n:
   c=a+b
   a=b
   b=c
   print(c)


a = int(input("Enter the first number of the fibonacci series... "))
b = int(input("Enter the second number of the fibonacci series... "))
n = int(input("Enter the number of terms... "))
print(a,b)
print("The numbers in fibonacci series are : ")
while(n-2):
   c=a+b
   a=b
   b=c
   print(c)
   n=n-1
   
#recursion
a,b=0,1
a
b
n = 7
print("fibonacci series are : ")
for i in range(0,n):
    if i<=1:
        c=i
    else:
      c=a+b
      a=b
      b=c
      print(c)
#recursion
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("positive number only")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# Driver Program
print(Fibonacci(9))

#Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l)
		
printValues()




import math as m
sq=m.pow(7,2)

def printValues():
    l = list()
    for i in range(1,11):
        l.append(m.pow(i,2))  
        if m.pow(i,2)>50:
            break
    
    print(l)
		
printValues()
     

def printValues():
    l = list()
    for i in range(1,21):
      if m.pow(i,2)>100:
          continue
      l.append(m.pow(i,2))
    print(l)
		
printValues()


#Write a Python program to detect the number of local variables declared in a function.

def test():
    """this is my first function"""
    x = 1
    y = 2
    s1= "Cdac Noida"
    print("Python programming")

print(test.__code__.co_nlocals)
print(test.__docstring__)


#lamda example
x = lambda y : y + 10
print(x(5))

#with many parameters
x = lambda y, z : y * z
print(x(10, 20))

a = lambda p, k, m : p + k + m
print(a(5, 6, 2))

def myfunc(n):
  return lambda a : a * n

#myfunc(7)


x=myfunc(7)
x(10)
