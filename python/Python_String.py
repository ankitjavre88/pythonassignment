a = "Hello"
print(a)

#string an array
a = "Hello, World!"
print(a[0])

#you get the length of a string, use the len() function.

a = "Hello, World!"
print(len(a))

#Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])
#get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

#the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

#negative indexes to start the slice from the end of the string

b = "Hello, World!"
print(b[-5:-2])