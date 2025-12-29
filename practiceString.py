#string built in functions/ methods

s = "   hello   "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s = "hello hello bye hello"
print(s.replace('hello', 'hlo', 2))

print(s.find('hello'))

s = 'helo'
print(s.upper())

s = "HelLLO"
print(s.lower())

print(s.swapcase())

stringTitle = "the fox jumps from the tree"
print(stringTitle.capitalize())
print(stringTitle.title())