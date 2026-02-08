userInput = input("Enter your value to know the Datatype: ")

try:
    value = eval(userInput)
except:
    value = userInput

noPrimitive = [str,list,tuple,set,dict]
Mutable = [list,set,dict]

print("This is Primitive or Immutable Datatype") if type(userInput) not in noPrimitive or type(userInput) not in Mutable else print("This is Mutable or Non-primitive Datatype")