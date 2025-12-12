# sort lists 
mylist =[1,12,3,4,5,6]
mylist.sort()
print(mylist)

my_Another_list = ['banana', 'Bano', 'apple', 'Aplle']
my_Another_list.sort()
print(my_Another_list)

my_Another_list1 = ['banana', 'Bano', 'apple', 'Aplle']
my_Another_list1.sort(key=str.lower)
print(my_Another_list1)

#reverse()
my_Another_list.reverse()
print(my_Another_list)
mylist.reverse()
print(mylist)

#list Comprehension

newList = [x for x in my_Another_list1 if "b" in x]
print(newList)

# list copy 
mynewList = [12,2,3,4,2,3,4,3,2]
empty_list = mynewList.copy()
print(empty_list)
empty2_list = list(mynewList)
print(empty2_list)
empty3_list = mynewList[:]
print(empty3_list)  

#list extend
list1 = [1,23,4,5,6]
list2 = ['a','b','c']

# for i in list2:
#     list1.append(i)
    
# print(list1)

# or using extend

list1.extend(list2)
print(list1)


# list methods 
# append()
# clear()
# copy()
# count()
# extend()
# index()
# insert()
# pop()
# remove()
# reverse()
# sort()

# Tuple 

thisTuple = ("apple", "banana", "cherry",)
y =("orange","yellow")
thisTuple += y

print(thisTuple) #it is working


#unpacking tuples 

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry",)

(green, yellow, *red) = fruits # *red takes all remaning value
print(green)
print(yellow); print(red)

#loop in tuple

for x in fruits:
    print(x)
    
for i in range(len(fruits)):
    print(fruits[i])
    
# while loop in tuple 

i = 0

while i<len(fruits):
    print(fruits[i])
    i += 1
    
# join tuples 

tuple1 = ("a", "b", "c")
tuple2 = (1,2,3,5,6,3,2,5,7,5,3,6,4,2,)

tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = tuple1 * 3
print(tuple4)

# tuple methods 
# count
tuple4 = tuple2.count(2)
print(tuple4)
# index 
print(tuple2.index(3))

#sets
# set is mutuable and unchangeable
# we can't assign new value to existed value, but we can remove or add the values 

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates, same thing with 0 and false:

thisSet = {2,0,3,4,5,"hello", 3.5, 2+2j, True, 1, False}
print(thisSet)
print(len(thisSet))

thisset2 = set((1,2,3,4,"hello", True))

thisset2.add("orange")
print(thisset2)

#update()

thisset2.update(thisSet)
print(thisset2)

# Remove Set Items

thisset2.remove(2)
thisset2.discard(3)
# we can also use pop but we don't know which item gonna removed from -1

del thisset2

# print(thisset2) not existed as we used del in before line

# loop sets 

for x in thisSet:
    print(x)
    
# python join sets 

# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

#union

set1 = {"a", "b", "c"}
set2 = {1,2,3}
set3 = {1.2,3.2,4.5,2.5}
myTuple = (1,2,3,4,5)
myList = [11,22,33,44,55]

set3 = set1.union(set2) #we can also use | opeartor for this
set4 = set1 | set2
set5 = set1.union(set2,set3)
set6 = set1.union(set2,set3,myTuple,myList)
print(set3, set4, set5,set6)


#update()
# Note: Both union() and update() will exclude any duplicate items.

set1.update(set2)
print("print",set1)

#intersection() or &
#here The intersection() method will return a new set, that only contains the items that are present in both sets.
set3=set3.intersection(set2) # only same items like ( duplicates)
print(set3)

#intersection_update()
# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

set1.intersection_update(set2)
print(set1)

# Difference or -
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {1,2,3,4,5,6}
set2 = {1,3,5,100,200,300}
set4 = set1.difference(set2)
print(set4) 

#symmetric Differences 
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set3 = set1.symmetric_difference(set2)
print(set3)

# python frozenset 
x = frozenset({"apple", "banana", "cherry"})
print(type(x))

#Dictionaries

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1002,
}

print(thisdict)
print(len(thisdict))
print(thisdict["brand"])

#get 

print(thisdict.get("model"))
#keys
print(thisdict.keys())
print(thisdict.values())
#values
print(thisdict)
thisdict.values()

#items
x = thisdict.items()
# every items like sets 
# print(x)

thisdict["price"] = 2000
print(thisdict)
print(x)

# change dictionary items 

thisdict["year"] = 2018
print(thisdict)

#update : argument should be dictionary not simply values example below

thisdict.update({"year": 2025})

# removing dictionary items 
# pop()
# thisdict.pop("model")
print(thisdict)

#popitem()
# thisdict.popitem()
print(thisdict) # remove the last inserted data in dictionary

# del
# del thisdict['brand']
print(thisdict)

# del can be also used to delete whole dict 
# del thisdict

#clear()
# thisdict.clear()
print(thisdict)

# loops in dict 

for x in thisdict:
    print(thisdict[x])
    
# values in loop 
for x in thisdict.values():
    print(x)
#keys in loop
for x in thisdict.keys():
    print(x)
#items
for x,y in thisdict.items():
    print(x,":",y)
    
# copy in dict 
newDic = thisdict.copy()
print(newDic)

# nested dictionaries 

parentdic = {
    "min1" : {
        "name": "prashant",
        "age": 21
    },
    
    "min2" : {
        "name": "rahul",
        "age": 20
    },
    
}

print(parentdic)
print(parentdic["min2"]["name"])

for i,obj in parentdic.items():
    print(i)
    for j in obj:
        print(j + ":", obj[j])
        
# dict methods 
# clear()
# copy()
# fromkeys()
# get()
# items()
# keys()
# pop()
# popitem()
# setdefault()
# update()
# values()

#python if statements
# elif, else 
# short-hand if 
if 5>3:print("hello world")
#shortHand if..else
a = 10
b = 20
bigger = a if a >b else b
print(bigger)

# multiple conditions on one line 
a = 300
b = 200
print('a') if a>b else print('equals') if a==b else print('b')

# logical operators in if..else 
a = 200
b = 33
c = 500
#and, or, not
if a>b and c>a:
    print("both are true")

# nested if 
#pass : does nthing but, left for futher logic