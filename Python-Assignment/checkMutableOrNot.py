userInput = eval(input("Enter your value to know the datatype: "))

try:
    value = eval(userInput)
except:
    value = userInput

mutableDt = [list,dict,set]

print("This is Mutable Data Type") if type(userInput) in mutableDt else print("This is Immutable Data Type")
