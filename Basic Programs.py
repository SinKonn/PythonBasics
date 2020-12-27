def prime():
	low = int(input("Enter Lower Limit: "))
	high = int(input("Enter Upper Limit: "))
	for var in range(low,high +1):
		if var > 1:
			for x in range(2,var):
				if (var % x) == 0:
					break
			else:
				print(var)
				


def fib():
	lmt = int(input("Enter limit for Fibonacci Series: "))
	n1, n2 = 0, 1
	count = 0
	if lmt <= 0:
		print("Enter positive number")
	else:
		while count < lmt:
			print(n1)
			n = n1 + n2
			n1 = n2
			n2 = n
			count += 1



def mul():
	x = int(input("View Multiplication table of: "))
	y = int(input("Upto limit: "))
	count = 1
	while count <= y:
		var = x * count
		print(var)
		count += 1



def fact():
	num = int(input("Enter number: "))
	print("The Factors are:")
	for var in range(1, num + 1):
		if num % var == 0:
			print(var)
		else:
			continue
		


def rand1():
	import random
	x = int(input("Enter lower limit: "))
	y = int(input("Enter upper limit: "))
	print(random.randint(x,y))



def leap():
	year = int(input("Enter year: "))
	if (year % 4) == 0:
		if (year % 100) == 0:
			if (year % 400) == 0:
				print("{0} is a Leap Year".format(year))
			else:
				print("{0} is not a Leap Year".format(year))
		else:
			print("{0} is a Leap Year".format(year))
	else:
		print("{0} is not a Leap Year".format(year))



def sort1():
	count = int(input("Enter the number of words: "))
	i = 1
	words = []
	while i < (count + 1):
		var = input("Enter word {0}: ".format(i))
		words.append(var)
		i += 1
	words.sort()
	print("The sorted words are:")
	for word in words:
		print(word)



def vowel_count():
	var = input("Enter String: ")
	vowel = set("aeiouAEIOU")
	count = 0
	for word in var:
		if word in vowel:
			count += 1
	print("Number of vowels is: ", count)

choice = int(input("Choose a task:\n1. Print Prime Numbers in Given Range\n2. Print Fibonacci series\n3. Multiplication Table\n4. Factors of Given Number\n5. Generate Random Number\n6. Leap Year Check\n7. Alphabetical Order Sort\n8. Number of Vowels in a String\nTask number: "))
if choice  == 1:
	prime()
elif choice == 2:
	fib()
elif choice == 3:
	mul()
elif choice == 4:
	fact()
elif choice == 5:
	rand1()
elif choice == 6:
	leap()
elif choice == 7:
	sort1()
elif choice == 8:
	vowel_count()
else:
	print("Invalid Selection")