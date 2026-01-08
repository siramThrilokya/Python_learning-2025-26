def addition(x,y):
    return print(f"{x} + {y} = ",x+y)

print("Give two numbers to sum")
while True:
    xinput = float(input("Enter the first value: "))
    yinput = float(input("Enter the second value: "))
    addition(xinput,yinput)