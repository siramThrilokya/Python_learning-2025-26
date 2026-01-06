expenses_list = []

while True:
    print('''
        press 'add' for adding expenses
        press 'show' for view your expenses
        press 'exit' for exit app
        ''')

    userChoice = str(input("Enter your choice: "))
    # while True:
    if userChoice.lower() == "add":
        while True:
            userInput = float(input("Enter your Expense, press '00' to stop: "))
            if userInput == 00:
                break
            expenses_list.append(userInput)
            # continue
    elif userChoice.lower() == "show":
            print("your expenses are : ", expenses_list)
        # break
    else:
        print("App as been exited")
        break
            # break


    
#     if userChoice == 1:
#     while True:
#         userInput = str(input("Enter your Expense, press 'exit' to stop: "))
#         if userInput.lower() == "exit":
#             break
#         expenses_list.append(float(userInput))
# elif userChoice == 2:
#     print("Your expenses are : ", expenses_list)
# else:
#     print("app as been exited")