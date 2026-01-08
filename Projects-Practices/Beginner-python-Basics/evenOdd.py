def even(x):
    return x%2 == 0

while True:
    userInput = int(input("Enter the value to know even or odd: "))
    returnedValue = even(userInput)
    if returnedValue == True:
        print("Given value is Even")
    else:
        print("Given value is Odd")

