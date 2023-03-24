#Return Double of n
def addition(n):
    return n+n

#We double all numbers using map()

number = (1,2,3,4)
result = map(addition,number)
print(list(result))