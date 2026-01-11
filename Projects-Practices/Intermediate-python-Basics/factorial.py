# Take a number as input and calculate its factorial.

def factorial(n):
    n = abs(n)
    if n==1 or n==0:
        return 1
    else:
     return n * factorial(n-1)

userInput = int(input("Enter your number to know the factorial: "))
print(factorial(userInput))