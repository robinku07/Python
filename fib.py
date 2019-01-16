"""
Write a program to generate first 'n' fibonacci series

Example usage:
--------------
    >>> fib(10)
    0 1 1 2 3 5 8 13 21 34

    >>> fib(20)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
"""


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


if __name__ == '__main__':
    from doctest import testmod
    testmod()


fib(8)