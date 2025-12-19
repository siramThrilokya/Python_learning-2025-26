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