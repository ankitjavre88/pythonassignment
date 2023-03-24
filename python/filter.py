ages=[23,18,17,19,20,21,22]

def filfun(x):
 if x<18:
  return False
 else:
  return True
adults= filter(filfun,ages)
for x in adults:
    print(x)