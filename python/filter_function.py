def fun(variable):
    letters = ['a','e','i','o','u']
    if(variable in letters):
        return True
    else:
        return False
    
sequence = ['g','e','e','j','k','s','p','r','o','o','o']
#using filter function

filtered = filter(fun,sequence)
print('The filtered letter are :')
for s in filtered:
    print(s)