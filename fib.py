def fib(n): # return Fibonacci series up to n
	"""Return a list containing the Fibonacci series up to n."""
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)    # see below
		a, b = b, a+b
	return result

num = 30000
print("Fibonacci series up to "+str(num)+' is')
print(fib(num))    # call it
print('total in %d numbers' %(len(fib(num))))