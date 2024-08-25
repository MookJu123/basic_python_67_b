"""
#
# Part : python function
# 
"""

def myFunction():
    i = 1
    while i <= 5 : 
        print("Hello world", i)
        i += 1
    else:
        print(" ")

myFunction()
myFunction()

# parameter
def myName(name):
    print("my name is",name)
myName("Anya")
myName("Loid")
myName("")

def myfullName(firstname = "unknown", lastname = "unknown"):
    print("my name is", firstname + " " + lastname )
myfullName("Anya", "Forger")
myfullName("Loid", "Forger")
myfullName("Yor", "forger")


def myFruit(fruits):
    for fruit in fruits :
        print(fruit)

fruits = ["apple", "banana", "coconut"]
myFruit(fruits)

def redPotion(hp):
    return hp + 50

print("HP: ", redPotion(100))
print("HP: ", redPotion(30))