
from functools import reduce

numbers = [4,2,3,5]
def sum(a,b):
    return a+b

#call sum() function on each element
total = reduce(sum,numbers)
print(total)