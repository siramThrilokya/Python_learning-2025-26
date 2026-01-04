# python inner classes 
# accessing inner class from the outside 
class Outer:
    def __init__(self):
        self.name = "Outer"

    class Inner:
        def __init__(self):
            self.name = "Inner"

        def display(self):
            print("hello world from inner class")

outer = Outer()
print(outer.name)
inner = Outer.Inner()
inner.display()

class Outer:
    def __init__(self):
        self.name = "prashant"

    class Inner:
        def __init__(self, outer):
            self.outer = outer
        
        def display(self):
            print(f"this is inner class function : {self.outer.name}")
        
outer = Outer()
inner = outer.Inner(outer)
inner.display()



# class Outer:
#   def __init__(self):
#     self.name = "Emil"

#   class Inner:
#     def __init__(self, outer):
#       self.outer = outer

#     def display(self):
#       print(f"Outer class name: {self.outer.name}")

# outer = Outer()
# inner = outer.Inner(outer)
# inner.display()



# example 

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()
        
    class Engine:
        def __init__(self):
            self.status = "off"

        def start(self):
            self.status = "Running"
            print("Engine started")

        def stop(self):
            self.status = "off"
            print("Engine stopped")
        
    def drive(self):
        if self.engine.status == "Running":
            print(f"Driving the {self.brand} {self.model}")
        else:
            print("Start the engine first!")
            
car = Car("Bmw", "i8")
car.drive()
car.engine.start()
car.drive()


class Computer:
    def __init__(self):
        self.ram = self.RAM()
        self.cpu = self.Cpu()
        
    class RAM:
         def store(self):
            print("storing data..!")
        
    class Cpu:
       def process(self):
            print("processing Data..!")
            
computer = Computer()
computer.ram.store()
computer.cpu.process()

# python file open 
print(" File Handling ".center(40, "*"))
# file handling
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.


f = open('demofile.txt', "rt")

# python file open 

f = open("demofile.txt")
# print(f.read())

f1 = open("files/demo2.txt")
print(f1.read())

# using with statement 
with open("demofile.txt") as f:
    print(f.read())
    
# closing file 

f = open("demofile.txt")
print(f.readline())
f.close()

# read only parts of the file 
with open("demofile.txt") as f:
    print(f.read(9))
    
# read lines - used to return one line
with open("demofile.txt") as f1:
    print(f1.readline())
    print(f1.readline()) # by calling two times we can access the 2 lines
    
    
# example though loops 
with open("demofile.txt") as f:
    for x in f:
        print(x)
        
# python file write 
# "a" for append
# "w" for write 

with open('demofile.txt', 'a') as f:
   f.write("now this is a modification line through code")

with open("demofile.txt") as f:
    print(f.read())
    
with open("demofile.txt", "w") as f:
    f.write("oops by mistake i deleted all my content")

with open("demofile.txt") as f:
    print(f.read())
    
# create a new file 
# x - for create, returns an error if the files exists 
# a - append and create a file if not exists
# w - write and create a file if not exists 

# f = open("myfile.txt", "x")
# f = open("files/myNewfile.txt", "x")

# to delete files 

import os
# os.remove("myfile.txt")

# check if file exist

# if os.path.exists("demofile.txt"):
#     os.remove("demofile.txt")
# else:
#     print("file removed or not existed")
    
# to delete folder 
os.remove("myfolder/demo.txt")
os.rmdir("myfolder") #i can remove only empty folder not filled folder