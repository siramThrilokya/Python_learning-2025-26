while True:
    userInput = str(input("Enter any word to know if it is palindrome or not & press 'stop' to end: ")).replace(" ", "").lower()
    reversedStr= userInput[::-1]
    if userInput == "stop":
        break
    elif userInput == reversedStr:
        print("yes, it's a palindrome word")
    else:
        print("No, it's not a palindrome word")
    