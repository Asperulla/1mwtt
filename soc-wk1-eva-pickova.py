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

#Bigger, better favorite number. 
#Write a program that asks for a person’s favorite number. 
#Have your program add 1 to the number, 
#and then suggest the result as a bigger and better favorite number. 
#(Do be tactful about it, though.)
fav_number = input("Write your favorite number: ")
print("Your favorite number is: " + fav_number + " but better number is "  + str(int(fav_number) + 1))
## pridat jeste type(), v pripade, kdy zada neco jineho nez cislo.

#Angry boss. Write an angry boss program that 
#rudely asks what you want. Whatever you answer, 
#the angry boss should yell it back to you and then fire you. 
#For example, 
#if you type in I want a raise, it should yell back like this:
boss = input("WHAT DO YOU WANT!? ")
print("WHAT DO YOU MEAN!! " + boss.upper() + "?!?" + " You are fired!!")
