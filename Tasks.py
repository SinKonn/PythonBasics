def task1():
	x = 1
	y = 0
	while x <100 :
		y = x + y
		x = x + 1
	print("The total is: %d" %y)


def task2():
	x = 25
	y = 0
	while x <50 :
		y = x + y
		x = x + 1
	print("The total is: %d" %y)


def task3():
	x = 0
	y = 0
	while x <99 :
		x = x + 1
		if x % 2 == 0:
			y = x + y
		else:
			continue
	print("The total is: %d" %y)


def task4():
	x = 5
	y = 0
	while x < 125:
		y = x + y
		x = x + 7
	print("The total is: %d" %y)


def task5():
	x = 1
	y = 1
	while x < 11:
		y = x * y
		x = x + 1
	print("The total is: %d" %y)


def task6():
	x = 1
	y = 100
	while x < 15:
		y = y - x
		x = x + 3
	print("The total is: %d" %y)
	
var = int(input("Which task wold you like? \n1. Add numbers from 0 to 99\n2. Add numbers from 25 to 49\n3. Add all even numbers from 0 to 99\n4. Add every 7th number from 5 to 124\n5. Multiply numbers from 1 to 10\n6. Start your sum at 100 and subtract every 3rd number from 1 to 14 \nTask "))
if var == 1:
	task1()
elif var == 2:
	task2()
elif var == 3:
	task3()
elif var == 4:
	task4()
elif var == 5:
	task5()
elif var == 6:
	task6()
else:
	print("Invalid Task!")