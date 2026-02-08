userInput = input("Enter your character: ")

if userInput.isalnum():
    listCon = list()
    listCon.append(userInput)
    print("It is not a special character", listCon)
else:
    print("It is a special character", str(userInput))