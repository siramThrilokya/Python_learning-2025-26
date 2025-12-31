# pip 

# import camelcase

# c = camelcase.CamelCase()

# txt = "hello world"

# print(c.hump(txt))

# python try except 

# try block is used to test a block of code for errors
# except block is used to handle the error 
# else block is used to execute the code when there is no error 
# finally block let you execute code, regardless of the result of the try and except blocks

print(" Exception Handling ".center(50, '*'))
# x = 10

try:
    print(x)
except:
    print("an exception occured")
    
# Many Exceptions 

try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")
    

# Else 

try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")

# Finally 
# this will definitely print even there is error or not 

try:
    print("x")
except:
    print("something went wrong")
finally:
    print("the try except is finished")
    

# Example pratice 

try:
    f = open("demofile.txt")
    try:
        f.write("lorum Ipsum")
    except:
        print("something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("something went wrong when opening the file")
    

# Raise an exception 
# As a Python developer you can choose to throw an exception if a condition occurs.

x = -1

# if x<0:
#     raise Exception("sorry, no number below zero")

# x = 'hello'

# if not type(x) is int:
#     raise TypeError("only integers are allowed")

print(" Python String formatting ".center(50, '*'))
# Python String formatting

# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# Before Python 3.6 we had to use the format() method.

price = 50
txt = f"the price is {price} dollars"
print(txt)

# example with 3 decimals points 

txt1 = f"the price is {price:.2f} dollars"
print(txt1)

# -> performing operations in f-strings

txt3 = f"the price is {20*50} dollars"
print(txt3)


# -> add taxes before displaying the price 

tax = 0.25
txt4 = f"the price is {price + (price * tax)} dollars"
print(txt4)

# -> if..else statements in the placeholders

txt5 = f"It is very {'expensive' if price >= 50 else "cheap"}"
print(txt5)

# -> execute functions in f-strings

