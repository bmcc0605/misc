#helper functions for assignment 4

#x to the nth power mod m
def square_and_multiply(x, n, m):
	if m == 1:
		return 0
	result = 1
	x = x%m
	y = x
	total = float(n)
	print "start"
	while n > 0:
		if n % 5000000 == 0:
			print n/total
		if(n % 2 == 1):
			result = (result * x) % m
		n = n - 1
		x = (x * x) % m
	print "finish"
	return result
