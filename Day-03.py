
def separator(e):
    print(e.center(40,"/"))


# Operators
# Arithmetic Operators 
# +, -, *, /, %, **, //
print(10+2)
print(10-2)
print(10*2)
print(10/2)
print(10%2)
print(10**2)
print(10//2)

#Assignment operators 
# =, +=, -=, *=, /=, %=, //==, **=, &=, |=, ^=, >>==, <<==, :=

x = 5
print(x)
x+=3
print(x)
x-=3
print(x)
x*=3
print(x)
x/=3
print(x)
x%=3
print(x)
x//=3
print(x)
x**=3
print(x)
# x &= 3
# print(x)
# # x|=3
# print(x)
# # x^=3
# print(x)
# # x>>=3
# print(x)
# # x<<=3
# print(x)
print(x:=3)
# print(x)

# Comparison operators 

a = 10
b = 30

print(a == b )
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# Logical operators
logic = "logical operators"
print(logic.center(40,"/"))

# and, or, not

print(x<5 and x<10)
print(x<5 or x<4)
print(not(x<5 and x<10))

# Identity operators
logic = "Identity operators"
print(logic.center(40,"/"))

# is, is not 
# whats differences between == and is ( where as == just check the values and is check for value and object in memory )

x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is y) # [False] the x and y both are same values but not same memory
print(x is not y) #True
print(x == y) # [True] its just check the values

# Membership operators
member = "Membership operators"
print(member.center(40,"/"))

# in, not in 
x = ["apple", "banana"]
print("banana" in x) #true
print("boy" not in x) #True boy is not in x that's true
print("boy" in x) #False boy is not in x

# Membership operators
separator("Bitwise operators")
# &,|,^,~,<<,>>
a = 10
b =5
print(a&b)
print(a or b)
print(a ^ b)
print(~a)
print(a<<2)
print(a>>2)

#Precedence Order
separator("Precedence Order")
# this shows the order and if operator is at same level like +,- comes in way precedence order then which one should go first is left->right approach when things follows in same level 
# 1. ()
# 2. **
# 3. +x, -x, ~x
# 4. *, /, //, %
# 5. +, -
# 6. <<, >>
# 7. &
# 8. ^
# 9. |
# 10. ==, !=, >, >=, <, <=, is, is not, in, not in
# 11. not
# 12. and
# 13. or

#List
separator("List")

myList = [1,2,3,4,"helow", 2.4, 1+0j]
print(myList)
anotherList = list((1,2,3,4,"23", 354.54, 15+2j)) #double round brackets
print(anotherList)

# list accesing 
myList[1]
myList[0:3]
myList[-3:-1]

thisList = ['mango', 'banana', 'apple', 'orange']
thisList[1:3]= ["kiwi", 'papaya'] # removed banana and apple as its comes under 1 and 2 index as shown [1:3] 3 not counted as n-1
print(thisList)


# insert 
thisList.insert(3, "treeOrange")
print(thisList) #['mango', 'kiwi', 'papaya', 'treeOrange', 'orange']

# add list items
#append items
# thisList = ['mango', 'banana', 'apple', 'orange']
thisList.append("kiwi") # add the kiwi in the last as mango,banana,apple,orange,kiwi
print(thisList) 
#Insert Items
thisList.insert(3, "treeOrange")
print(thisList) #['mango', 'kiwi', 'papaya', 'treeOrange', 'orange']
#Extend List
vegetables = ["Carrot", "Spinach", "Cauliflower", "Brinjal"]
thisList.extend(vegetables)
print(thisList)
mytuple = (1,2,3,4,5,)
thisList.extend(mytuple)
print(thisList) #['mango', 'kiwi', 'papaya', 'treeOrange', 'treeOrange', 'orange', 'kiwi', 'Carrot', 'Spinach', 'Cauliflower', 'Brinjal', 1, 2, 3, 4, 5]
#removes
thisList.remove(1)
print(thisList)
#pop(index)
thisList.pop()
print(thisList)
thisList.pop(-2)
print(thisList)

# del keyword for remove
del thisList[-3]
print(thisList) #brinjal removes[or deleted completely]
#clear keyword
thisList.clear()
print(thisList) #empty list

#Loop lists
#for in list
mylist = ["apple", "banana", "cherry"]
for x in mylist:
    print(x)
    
# loop through the index numbers 
for i in range(len(mylist)):
    print(mylist[i])
    
# using the while loop 
i = 0
while i<len(mylist):
    print(mylist[i])
    i = i+1
    
# list comprehension
mySecondList = ['apple', 'banana', 'blackberry']
[print(x) for x in mySecondList]