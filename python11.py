"""
#
# Part : python try except
# 
"""
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

try :
    print(x)
except NameError as e:
    print("not defined: " , e)   
except Exception as e:
    print("sonething else went wrong!", e)

try:
    print("Hello world!")
except:
    print("something went wrong!")
else:
    print("nothing went wrong1")

try:
    print(x)
except:
    print("something went wrong!")
finally:
    print("Finished!!!")

# x = -1
# if x < 10:
#    raise Exception("sorry, number below zero")

x = "Hello"
if not (type(x) is int):
    raise TypeError("Only integers are allowed")




