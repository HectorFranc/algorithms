def factorial(n):
    '''
    Returns n! (n factorial)
    Parameters:
    n: number non-negative
        Number that will be used
    '''
    n = int(n)
    if n < 0:
        raise RecursionError('n is < 0. n should be >= 0')
    else:
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
