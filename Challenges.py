def c1():
	print("CHALLENGE 1:")
	String1 = "New String"  #Assigning new string
	print("String is: %s" %String1)
	String2 = String1.upper()  #Switching to uppercase
	print("Switching to UPPERCASE: %s" %String2)
	strlen = len(String1) #calculating string length
	print("String length is: %d" %strlen)
	#splitting String1
	fhalf = String1[:5]
	shalf = String1[5:]
	print("First half is: %s" %fhalf)
	print("Second half is: %s" %shalf)

def c2():
	name = input("Enter your name:")
	print("Your name is: %s" %name)
	uppern = name.upper()
	print("Uppercase is: %s" %uppern)
	namelen = len(name)
	print("The length of you name is: %d" %namelen)
	x = 0
	while x <= namelen:
		print(name[x-1:x])
		x = x+1


def c3():
	myList = []
	capList = []
	x = 0
	z = 0
	while x < 2:
		x = x+1
		var = input("Enter string number %d: " %x) #using a variable since input can't directly go into list
		myList.append(var) #accepting user input string into list
	for y in myList:
		print(y)
	
	capList = [z.lower() for z in myList] #converting to lowercase
	print("Lower case is: ")
	for y in capList:
		print(y)

	for z in myList:
		stlen = len(z)
		print("Length of string %s is: %d" %(z, stlen))
	print("First 2 characters of the string are: ")
	for z in myList:
		print(z[:2])
	print("Last 2 characters of the string are: ")
	for z in myList:
		print(z[-2:])
		
c = int(input("Which challenge would you like?\nChallenge 1\nChallenge 2\nChallenge 3\n"))
if c == 1:
	c1()
elif c == 2:
	c2()
elif c == 3:
	c3()
else:
	print("Invalid Selection!")