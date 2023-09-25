myString = "This is a string."
print(myString)
print(myString + " is of the data type " + str(type(myString)))

name = input("What is your name? ")
print(name)
color = input("what is your favourite color?")
animal = input("what is your facourite animal?")
print("{}, you like a {} {}!".format(name,color,animal))