# Check if a string is palindrome (ignore case & spaces)
userChoice = False
while userChoice==False:
    userInput = str(input("Enter any word to know if it is palindrome or not:\t"))
    userInput.split()
    if " " in userInput:
        print("please make sure to remove spaces")
    else:
        reversedStr= userInput[::-1]
        reversedStr.split()
        if userInput.lower() == reversedStr.lower():
            print("yes, it's a palindrome word")
        else:
            print("No, it's not a palindrome word")
    

# print(userInput)
# print(reversedStr)