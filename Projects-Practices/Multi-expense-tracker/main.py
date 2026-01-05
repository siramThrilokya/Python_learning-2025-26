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
        userInput = str(input("Enter your Expense, press 'exit' to stop: "))
        if userInput.lower() == 'exit':
            break
            # continue
    elif userChoice.lower() == "show":
        if expenses_list[-1] == 'exit':
            expenses_list.pop()
            print("your expenses are : ", expenses_list)
        else:
            print("Your expenses are : ", expenses_list)
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