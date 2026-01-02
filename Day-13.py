# python class properties 

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Prashant", 21)

print(p1.name)
print(p1.age)

# modify properties 

class Car:
    def __init__(self, Cname, Cmodel):
        self.Cname = Cname
        self.Cmodel = Cmodel
        
c1 = Car("BMW", "i8")
c1.Cmodel = "i9"


# delete properties 

del c1.Cmodel

print(c1.Cname)
# print(c1.Cmodel)

# class properties vs object properties 

class Person:
    species = "Human"

    def __init__(self,name, age):
        self.name = name
        self.age = age
        

p3 = Person("Prashant", 21)

print(p3.name)
print(p3.age)
print(p3.species)


# modifying class properties 

class Person:
    event = ""

    def __init__(self, name):
        self.name = name
        
p4 = Person("prashant")

p4.event = "evening"

print(p4.name)
print(p4.event)

# adding new properties 

class Job:
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
j1 = Job("laptop", "electronics")
print(j1.name)
print(j1.type)

j1.brand = "macbook"
j1.price = 100000

print(j1.brand)
print(j1.price)


# class methods 
print(" Class Methods ".center(40, "*"))

class Calculator:
    def addition(self, a,b):
        return a + b
    
    def mutilple(self,a,b):
        return a * b
    
calc = Calculator()
print(calc.addition(10,2))
print(calc.mutilple(10,2))

# methods accessing properties 

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def greet(self):
        return (f"my name is {self.name} and i'm {self.age} years old")
        
p5 = Person("Prashant", 21)

print(p5.greet())


# methods modifying properties 

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def Birthday(self):
        self.age += 1
        print(f"happy birthday you are now {self.age} years old")

p6 = Person("prashant", 21)
# print(p6.Birthday())
p6.Birthday()
p6.Birthday()
# print(p6)

# __str__() methods 

print(p6) #<__main__.Person object at 0x10315a3c0>. [ when i try to print the object it self without any properties then its show some memory allocation address, by using __str__ we are telling that when i print object then print some default context present in __str__() method]

class Person:
    
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} demo trial {self.age}"
    
p7 = Person("prashant", 21)
print(p7)

# example of small add,remove and display class 

class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []
        
    def addSongs(self,song):
        self.songs.append(song)
        print(f"Song added : {song}")
        
    def removeSong(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Song removed: {song}")
            
    def displayInfo(self):
        print(f"playlist : {self.name}")
        for index, song in enumerate(self.songs):
            print(f"{index+1}: {song}")
            
            
playlist = Playlist("favorites")
playlist.addSongs("HeatWaves")
playlist.addSongs("closer")
# playlist.removeSong("closer")
# playlist.removeSong("closer")
playlist.displayInfo()

# delete methods

class Person:
    def __init__(self,name):
        self.name = name
    
    def greet(self):
        print(f"hello, {self.name}")

p8 = Person("prasxor")
del p8.greet
# p8.greet() 