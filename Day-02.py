# strings ( strings are arrays )
a = "hello world"
print(a[1])

# string looping 
for x in a:
    print(x)
    
# length in string
print(len(a))

#present in string
txt = "my name is prashant kumar sinha"
print("prashant" in txt) #true

# if statement with present 
if "prashant" in txt:
    print("yes, 'prashant' is present in txt")
    
#check if not
print('rahul' not in txt) #true

#if statement with if not
if "rahul" not in txt:
    print("yes, 'rahul' is not present in txt")
    
# python slicing strings
str = 'prashant'
# print(str[1:4])
# print(str[-5:-1]) [greater value : smallest value]

# python - modify strings 
# upper
ex = 'hello, world'
print(ex.upper())
# lower
ex1 = 'HELLO WORLD'
print(ex1.lower())
# strip
ex2 = "    hello world!   "
print(ex2.strip()) #removes spaces from front and end
# replace
print(ex.replace("hello", "bye"))
# split 
print(ex.split(",")) #make separation using comma in list

#string concatenation
a = "hello"
b = "world"
c = a+ " " +b
print(c)

# string format 
age = 22
name = "prashant"
txt = f"my name is {name} and my age is {age}"
print(txt)

#:.2f format
price = 200
txt1 = f"I sell my product at {price:.2f} and get {1+1}" # float of .00
print(txt1)

# escape characters 
txt2 = "we are so-called \"vikings\" from the north"
print(txt2)

#\' single quote
esc = 'hello world \'bye\''
print(esc)
# \\ backslash
esc1= 'hello world \\ hello' #to use single backslash we need to type two times 
print(esc1)
# \n new line 
esc2 = 'hello \nworld'
print(esc2)
print("/////////////////////")
#\r carraige return
esc3 = "Hello\rWorld"
print(esc3)
#\t
esc4 = "bring\tworld"
print(esc4)

#strings methods [ all string methods return new values. they do not change the original string]
print('//////////string methods//////////')
#capitalize() - converts the first character to upper case
txt = "hellO World"
print(txt.capitalize())
#casefold() - converts string into lower case
print(txt.casefold())
#center - returns a centered string
print(txt.center(20,"/"))
#"@".join()
myTuple = ('apple', 'ball', 'cat')
xjoin = "#".join(myTuple) #=apple#ball#cat
print(xjoin)
# count()
txtcount = " I love cars and codes and cars are best."
xcount = txtcount.count("cars") #count in the sentences for content how many times its repeated
print(xcount)
#endswith(value,startindex,endindex)
x_endswith = txtcount.endswith('.') #true
x_endswith_2 = txtcount.endswith('.', 0,20) # false ( index 0 to 20)
print(x_endswith)
print(x_endswith_2)
#find()
x_find = txtcount.find('codes')
print(x_find)
#format
txtz = "for only {price:.2f} dollars"
print(txtz.format(price=100))
txty = "I love cars and {programming_language} and {car_name} are best."
print(txty.format(programming_language="python", car_name="Mustag"))
#isalpha()	Returns True if all characters in the string are in the alphabet
# isdigit()	Returns True if all characters in the string are digits
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isupper()	Returns True if all characters in the string are upper case
# startswith()	Returns true if the string starts with the specified value

#list/Array 
#append()
myList = [1,12,3,4,5,3]
mySecondList = [100, 200, 400]
myList.append(6)
# print(myList)
#clear()
# myList.clear()
#copy()
my_another_list = myList.copy()
print(my_another_list)
print(myList)
#count()
print(myList.count(3)) #its count 3 how many present in mylist
#extend()
myList.extend(mySecondList)
print(myList)
#index()
print(myList.index(100))
#insert()
myList.insert(7,1000)
print(myList)
print(myList.index(100))
#pop()
myList.pop()
print(myList)
#remove
myList.remove(1000)
print(myList)
#reverse()
myList.reverse()
print(myList)
#sort()
myList.sort()
print(myList)
myList.sort(reverse=True)
print(myList)

#boolean
print(bool("hello"))
print(bool(""))
print(bool())
print(bool(1))
print(bool([]))
print(bool([1,2,3]))
print(bool((1,2,30)))
print(bool(()))
print(bool({}))
print(bool({name:"prashant", age:25}))

print(isinstance(myList, tuple)) #its check whether the mylist is tuple or not (false), mylist is list not tuple thats why false
