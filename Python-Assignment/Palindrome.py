userInput = str(input("Enter the word to know the palindrome of it : "))

myDict = dict()

def keyvalue(val):
    reversedStr = val[::-1]
    myDict[val] = reversedStr
    print(myDict)
    
    
keyvalue(userInput) if userInput == userInput[::-1] else print((userInput+"\n")*3)

del myDict