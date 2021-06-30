"""

This is the "example" module.

the example module supplies one function, factorial(). For example

>>> factorial(5)
120


"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0
    
    >>> [factorial(n) for n in range(6)]  
    [1,1,2,6,24,120]
    >>> factorial(30)
    >>> factorial(-1) 
    >>> factorial(30.0) 
    >>> factorial(1e100)

    """

    import math
    if not n >= 0:
        raise ValueError("n must be >=0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")

    if n+1 == n: #catch a value like 1e300
        raise OverflowError("n too large")
    result =1
    factor =2
    while factor <= n:
        result *= factor
        factor += 1
    return result


    if __name__ == "__main__":
        import doctest
        doctest.testmod()
        




