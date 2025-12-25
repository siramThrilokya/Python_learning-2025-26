Listly = [1,2.3,1+2j,"hello", "world", True, None, 34, 54,2.234, 13,2.0, "gowtham"]


integer = 10
floatly = 1.4
complexly = 1+2j
string = "hello"

def collection(myList):
    numbers = []
    strings = []
    others = []
    for item in myList:
        if isinstance(item, (int,float,complex)) and not isinstance(item, bool):
            numbers.append(item)
        elif isinstance(item, str):
            strings.append(item)
        else:
            others.append(item)
    
    return numbers,strings,others

numbers,strings,others = collection(Listly)
# print(numbers,strings,others)
print("Numbers are : ", numbers)
print("Strings are : ", strings)
print("Others are : ", others)

# print(Listly)