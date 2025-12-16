# create an iterator

# __iter__(), __next__()


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myClass = MyNumbers()
myiter = iter(myClass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# for x in myiter:
#     print(x)  #dont run this its goes endless cause its dont have limit use above print(next) statement for only 5 times run

# stopIteration 
# to deal with no limit iteration of the iterators we need stopIteration

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration
        
myclass2 = MyNumbers()
myiter2 = iter(myclass2)

for x in myiter2:
    print(x)

# python modules 
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

import Mymodule as mx
import platform

mx.greeting("prashant")
a = mx.person1["age"]
print(a)

x = platform.system()
print(x)

# using the dir() function 

# y = dir(platform)
# print(y)
print(platform.processor())


# import from module 

from Mymodule import person1

print(person1["age"])

# python datetime 

# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

import datetime

x = datetime.datetime.now()
print(x)

# return the year and name of weekday


print(x.year)
print(x.month)
print(x.day)

# creating date objects 

xy = datetime.datetime(2020,5,17)
print(xy)

# the strftime() method

print(xy.strftime("%B"))
print(xy.strftime("%A"))
print(xy.strftime("%C"))

# python math 
# Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

minify = min(10,20,33,0.3, 1)
print(minify)

list = [10,1,230,405,60,30,503]

# print(min(list))

def find_min_value(arg):
    minimum_value = float('inf')
    if len(arg) == 0:
        return 0
    else:
        for current_value in arg:
            if current_value< minimum_value:
                minimum_value = current_value
        return minimum_value
    
print("minimum value is :", find_min_value(list))

print(max(list))

# abs() : The abs() function returns the absolute (positive) value of the specified number:

mera_value = abs(-108.23)
print(mera_value)

# pow(x,y) - Return the value of 4 to the power of 3 (same as 4 * 4 * 4):

mera_dursra_value = pow(4,3)
print(mera_dursra_value)

# the math module 

import math

x = math.sqrt(81) # 9*9 = 81
print(x)

# math.ceil()

xx = math.ceil(1.4) # 2
yy = math.floor(1.6) # 1

print(xx); print(yy)

# math.pi() pi(3.14...)

yyy = math.pi
print(yyy)
