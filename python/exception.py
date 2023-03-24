#try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")
  
#Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
 # the try block does not generate any error:
 
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
  #finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")