# python json 
# json is a syntax for storing and exchanging data
# JSON is text, written with js object notation 

import json

# converting from json to python 

#some json
x = '{"name" : "prashant", "age": 22, "city": "new york"}'

# parse x:
y = json.loads(x)

# the result is a python dictionary 
print(y["age"])

# converting from python to json

# xx is a python object (dict)
xx = {"name": "prashant",
      "age": 30,
      "gender": "male"}

# convert into json 
yy = json.dumps(xx)

# the result is a json string 
print(yy)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))