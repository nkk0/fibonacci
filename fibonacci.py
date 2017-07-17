def fibonacci():
	n = int(input('Enter a number: '))
	while n < 1:
		print('Enter a positive number bigger than 0')
		n = int(input("Enter a number: "))
	a = 0
	b = 1
	if n == 1:
		print('The 1st number in the fibonacci sequence is 0.')
	elif n == 2:
		print('The 2nd number in the fibonnaci sequence is 1.')
	else:
		for _ in range(n - 2):
			c = a + b
			a = b
			b = c
		if n % 10 == 1 and n != 11:
			suffix = 'st'
		elif n % 10 == 2 and n != 12:
			suffix = 'nd'
		elif n % 10 == 3 and n != 13:
			suffix = 'rd'
		else:
			suffix = 'th'
		print('The {}{} number in the fibonacci sequence is {}.'.format(n, suffix, c))
	fibonacci()

fibonacci()
