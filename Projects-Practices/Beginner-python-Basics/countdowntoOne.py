# Take a number n and print a countdown from n to 1.

while True:
    userinput = int(input("Enter your number to start countdown: "))
    for i in range(userinput,0,-1):
        print(i)