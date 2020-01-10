def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        a = n* fib(n-1)
        return a
