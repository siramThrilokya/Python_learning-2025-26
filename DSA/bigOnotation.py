number = [3,6,2,4,3,6,8,9]
duplicate = None

for i in range(len(number)):
    for j in range(i+1, len(number)):
        if number[i] == number[j]:
            duplicate = number[i]
            break