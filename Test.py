my_list = []

def add(e):
   summly = sum(e)
   return summly
def maxValue(e):
    maxly = max(e)
    return maxly
def minValue(e):
    minily = min(e)
    return minily
def avg(e):
    avg_value = sum(e)/len(e)
    return avg_value

while True:
    user_input = input("Enter the your value and press 'stop' to end: ")
    if(user_input.lower() =="stop"):
        break
    my_list.append(int(user_input))
    
    print("your list :",my_list)
   

print("your list is", my_list)
print("sum total: ", add(my_list))
print("max value: ", maxValue(my_list))
print("min value: ", min(my_list))
print("avg value: ", avg(my_list))
