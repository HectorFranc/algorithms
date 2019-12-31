def factorial(n):
    n = int(n)
    if n < 0:
        raise RecursionError('n is < 0. n should be >= 0')
    else:
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
