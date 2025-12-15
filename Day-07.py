# python lamba 

# Lambda Functions
# A lambda function is a small anonymous function.

x = lambda a : a+10

print(x(5))

# multiple lambda function 

y = lambda i,j : i*j

print(y(10,2))

# why use lambda function 

def myfunc(n):
    return lambda a : a+n

result = myfunc(10)

print(result(20))

# we can use same function to modify the n value and assigning to one variable 

result1 = myfunc(200)
print(result1(10))

# lambda with built-in functions 

# map()
numbers = [1,2,3,4,5]
doubled = list(map(lambda x : x*2, numbers))
print(doubled)

# getting cube of list values using map()
triples = list(map(lambda x : x *3, numbers))
print(triples)

# filter()

odd_numbers = list(filter(lambda x : x%2 != 0, numbers))
print(odd_numbers)

even_numbers = list(filter(lambda x : x%2 == 0, numbers))
print(even_numbers)

# sorted()
students_data = [("hello", 21), ("zprashant", 22), ("arahul", 22)]
sortedValue = sorted(students_data, key=lambda x : x[0])
print(sortedValue)

# sort strings by length

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

# python recursion 
# Recursion is when a function calls itself.


def countdown(n):
    # base case 
    if n<=0:
        print("done!")
    # recursive case 
    else:
        print(n)
        countdown(n-1)
    
# countdown(99)

# Without a base case, the function would call itself forever, causing a stack overflow error.

def factorial(n):
    # base case 
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))

# fibonacci sequence 

# 0,1,1,2,3,5,8,13,21,34. new number is sum of past two values like 1,1 = 2, 1,2 = 3, 2,3 = 5, 3,5= 8 etc...

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# recursion with list - sum of the list values

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

print(sum_list(numbers))

# recursion depth limit 
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

# function generators 
# Generators are functions that can pause and resume their execution.

def my_generator():
    yield 1
    yield 2
    yield 30
    
for value in my_generator():
    print(value)

# Generators allow you to iterate over data without storing the entire dataset in memory.
# Instead of using return, generators use the yield keyword.

def count_upto(n):
    count = 1
    while count<= n:
        yield count
        count +=1
    
for num in count_upto(5):
    print(num)
    
# Unlike return, which terminates the function, yield pauses it and can be called multiple times.

# generators saves memory 

def large_sequence(n):
    for i in range(n):
        yield i

gen = large_sequence(100000)
print("count from here")
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen)) #3 times the function runs like 0,1,2,3

# stopIteraton exception 

def simple_gen():
    yield 1
    yield 2
    
gen = simple_gen()

print(next(gen))

# generator expressions 

#generator methods
# send() and close()

# python range 
# range(start,stop,step )

xyy = range(10)
print(list(xyy))

# print(range(10))

for i in range(20):
    print(i)
    
print(list(range(5,15)))
print(list(range(5,15,2)))

# slicing ranges

r = range(10,20)
print(r[9])

# membership testing 
print(12 in r)
print(len(r))


# python arrays 
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
# Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.

# in w3schools arrays are showen as list same syntax without any changes or catch different same methods to insert and remove 


# Python Iterators
# An iterator is an object that contains a countable number of values.

# an iterator is an object which implements the iterator protocol, which consist of the methods 
# __iter__(), __next__() 

# iterator vs iterable 
# lists,tuples,dicitionaries,and sets are iterable objects 

mytuple = ('apple', 'banana','cherry')
myitr = iter(mytuple)

print(next(myitr))
print(next(myitr))
print(next(myitr))

# try with string 

name = "prashant"

op = iter(name)

print(next(op))
print(next(op))
print(next(op))
print(next(op))
print(next(op))
print(next(op))
print(next(op))
print(next(op))

# looping through an iterator 

mytuple = ("apple", "banana", "cherry")