# 2023-01-06 input the limit of Fibonacci series to generate

def fib(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result


num = int(input("Please enter the limit of last Fibonacci series:"))
print("Fibonacci series up to "+str(num)+' is')
print(fib(num))    # call it
print('total in %d numbers' % (len(fib(num))))
