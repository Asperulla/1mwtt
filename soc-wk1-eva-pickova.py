##***day1***

#Hours in a year. How many hours are in a year?
print(365*24)
#8760

#Minutes in a decade. How many minutes are in a decade?
common_year = 365*24*60
leap_year = 366*24*60
print(8*common_year + 2*leap_year)
#5258880

#Your age in seconds. How many seconds old are you?
print(34*365*24*60*60)

#Andreea Visanoiu: I'm 48618000 seconds old hahaha. 
#Calculate @Andreea Visanoiu's age.
print(48618000/365/24/60/60)

##***day3***

#Full name greeting. Write a program that asks for a person’s 
# first name, then middle, and then last. Finally, 
# it should greet the person using their full name.
first = input("Write your first name: ")
middle = input("Write your middle name: ")
last = input("Write your last name: ")
print("Hello "+ " "+ first + " " + middle + " " + last + "!")
