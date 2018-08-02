
#99bottles
for bottle in range(0, 98):
	print (str(99 - bottle) + " bottles of beer on the wall, " + str(99 - bottle) + " bottles of beer. "
		" Take one down and pass it around, " + str(99 - bottle - 1) + " bottles of beer on the wall."
		)
	bottle = bottle - 1
	
print("1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.")
print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")

#more exactly:
for bottle in range(0, 97):
	print (str(99 - bottle) + " bottles of beer on the wall, " + str(99 - bottle) + " bottles of beer. "
		" Take one down and pass it around, " + str(99 - bottle - 1) + " bottles of beer on the wall."
		)
	bottle = bottle - 1

	
print(
	"2 bottles of beer on the wall, 2 bottles of beer. 
      Take one down and pass it around, 1 bottle of beer on the wall.
      1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, 
      no more bottles of beer on the wall. 
      No more bottles of beer on the wall, no more bottles of beer. 
      Go to the store and buy some more, 99 bottles of beer on the wall."
     )
