# python inheritance 

# create a parent class. 
# parent class 
class Person:
    def __init__(self,fname, lastname):
        self.fname = fname
        self.lastname = lastname
        
    def printname(self):
        print(self.fname, self.lastname)

        
x = Person("john", 'doe')
x.printname()

# child class 
class Student(Person):
    pass

s = Student('prashant', 'kumar')
s.printname()

# add the __init__() function
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

class Student1(Person):
    def __init__(self,fname,lastname):
        Person.__init__(self,fname,lastname) # this will keep inheritance of the parent class
        

# super() function 
class Student2(Person):
    def __init__(self,fname,lastname):
        super().__init__(fname,lastname)
        
# add propeties 
class Student3(Person):
    def __init__(self,fname,lastname):
        super().__init__(fname,lastname)
        self.graduationyear = 2026
        
# adding year parameter 
class Student4(Person):
    def __init__(self,fname, lastname,year):
        super().__init__(fname,lastname)
        self.graduationyear = year
        
x1 = Student4('rahul','solanki',2024)
print(x1.fname)
print(x1.lastname)
print(x1.graduationyear)

# add methods 
class Student5(Person):
    def __init__(self,fname,lastname,year):
        super().__init__(fname,lastname)
        self.graduationyear = year
        
    def printAll(self):
        print(f'welcome ! {self.fname} {self.lastname} in the passing year of {self.graduationyear}')

x2 = Student5("prashant", "kumar", 2026)
x2.printAll()

# Polymorphism 
# single function/methods/operator used as many forms 

# function polymorphism 
# len(var) - len can be used in str,tuple,list etc..

mystr = "hello world"
print(len(mystr))

myTuple = (12,3,4,5,5)
print(len(myTuple))

mydict = {
    "name": "prashant",
    "age": 21,
    "gender": "male"

}

print(len(mydict))

# class polymorphism 

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("drive !")
        
class Ship:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("sail !")
        
class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("fly !")
        
car1 = Car("bmw", "i8")
ship1 = Ship("ibiza", "touring 20")
plane1 = Plane("boeing", "747")

for x in (car1,ship1,plane1):
    x.move()
    

# inheritance class polymorphism 

class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("move!")

class Car(Vehicle):
    pass

class Ship(Vehicle):
    def move(self):
        print('sail..')

class Plane(Vehicle):
    def move(self):
        print("fly..!")

car2 = Car("bmw", "i7")
ship2 = Ship("titanic", "243")
plane2 = Plane("Airbus", "787")

for x in (car2,ship2,plane2):
    print(x.brand)
    print(x.model)
    x.move()
    
# python encapsulation 

# Encapsulation is about protecting data inside a class

# private properties 

class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age #(__ is used to declare private property)
    
p1 = Person("Prashant", 21)
print(p1.name)
# print(p1.__age) # error : AttributeError: 'Person' object has no attribute '__age' 

# Note: Private properties cannot be accessed directly from outside the class.
# To access a private property, you can create a getter method:

# example for private property access throught getter method 

class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
        
    def getInfo(self):
        return self.__age
    
p1 = Person("Prashant", 21)
print(p1.getInfo())


# set private property value 
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.__age = age
        
    def getAge(self):
        return self.__age
    
    def set_age(self,age):
        if age>0:
            self.__age = age
        else:
            print("age must be positive")

p2 = Person("prashant", 29)
print(p2.getAge())

p2.set_age(200)
print(p2.getAge())

# why use encapsulation 
# 1. data protection
# 2. validation
# 3. flexibility
# 4. control

class Student:
    def __init__(self,name):
        self.name = name
        self.__grade = 0
        
    def set_grade(self,grade):
        if 0<= grade <= 100:
            self.__grade = grade
        else:
            print("grade should be between 0 and 100")
            
    def get_grade(self):
        return self.__grade
    
    def get_status(self):
        if self.__grade >= 60:
            return "passed"
        else:
            return "failed"

s1 = Student("prashant")
s1.set_grade(72)
print(s1.get_grade())
print(s1.get_status())

# protected properties 

class Person:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

p5 = Person("prashant", 10000000)
print(p5.name)
print(p5.__salary) # error: we can't access the private property outside directly we need to use getter