"""
Your module description
"""
myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("Siapa nama Anda? ")
print(name)

color = input("Apa warna kesukaan Anda? ")
animal = input("Apa hewan kesukaan Anda? ")
print("{}, Anda suka dengan  {} {}!".format(name,animal,color))
