myList = []

print("Enter the values to add in list")
while True:
    listValues = int(input("Enter the values and '00' for exit: "))
    if listValues == 00:
        print(myList)
        break
    myList.append(listValues)

def TotalSum(x):
    minvalue = 0
    i = 0
    print(len(x))
    while i<=len(x)-1:
        if x[i]>= minvalue:
            minvalue = x[i]
        i = i+1
    print("max value in list is: ",minvalue )

TotalSum(myList)