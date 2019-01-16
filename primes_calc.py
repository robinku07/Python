# coding: utf-8
# %load http://tinyurl.com/primes-ex
"""
Preliminary exercise
====================
Kindly read and follow the instructions as below:

Complete the program by implementing the functions is_prime()
and print_primes().

When this program is saved as 'primes_exercise.py' and executed using the
command 'python primes_exercise.py -v' at the shell prompt or windows command
prompt (with python installed), the doctest test cases are run. Ensure that
all test cases are passed as 'ok.'

Example module level tests
--------------------------
   >>> print_primes(10)
   2 3 5 7 11 13 17 19 23 29

   >>> is_prime(32)
   False

   >>> print_primes(15)
   2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

   >>> is_prime(37)
   True

How to test the program
-----------------------
    bash:~/Training/Core_Python$ python primes_exercise.py -v
    Trying:
        print_primes(10)
    Expecting:
        2 3 5 7 11 13 17 19 23 29 
    ok
    Trying:
        is_prime(32)
    Expecting:
        False
    ok
    Trying:
        print_primes(15)
    Expecting:
        2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 
    ok
    Trying:
        is_prime(37)
    Expecting:
        True
    ok
    Trying:
        is_prime(2)
    Expecting:
        True
    ok
    Trying:
        is_prime(27)
    Expecting:
        False
    ok
    Trying:
        is_prime(23)
    Expecting:
        True
    ok
    Trying:
        is_prime(127)
    Expecting:
        True
    ok
    Trying:
        is_prime(129)
    Expecting:
        False
    ok
    Trying:
        print_primes(10)
    Expecting:
        2 3 5 7 11 13 17 19 23 29 
    ok
    Trying:
        print_primes(20)
    Expecting:
        2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 
    ok
    3 items passed all tests:
       4 tests in __main__
       5 tests in __main__.is_prime
       2 tests in __main__.print_primes
    11 tests in 3 items.
    11 passed and 0 failed.
    Test passed.

"""


def is_prime(number):
    """
    Returns True if number is prime, else returns False

    Check for primality of number should be performed by trying to divide the
    number by a sequence of integers starting from 2 to square root of number.

    Example usage:
    --------------
        >>> is_prime(2)
        True

        >>> is_prime(27)
        False

        >>> is_prime(23)
        True

        >>> is_prime(127)
        True

        >>> is_prime(129)
        False

    """
    for r in range(2, int(number ** 0.5)+1):
        if number % r == 0:
            return False
    return True


def print_primes(n):
    """
    Print a series of first n prime numbers starting from 2. Primality check
    of each number from 2 to n is performed by using is_prime() function (to
    be implemented) above.

    Example usage:
    --------------
        >>> print_primes(10)
        2 3 5 7 11 13 17 19 23 29 


        >>> print_primes(20)
        2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 

    """
    i = 2
    while n:
        if is_prime(i):
            print(i,end=" ")
            n -= 1
        i+=1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
