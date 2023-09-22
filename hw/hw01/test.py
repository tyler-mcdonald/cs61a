# from hw01 import largest_factor
# def largest_factor_test():
#     assert largest_factor(15) == 5, 'The largest factor of 15 should be 5'
#     assert largest_factor(80) == 40, 'The largest factor of 80 should be 40'
#     assert largest_factor(13) == 1, 'The largest factor of 13 should be 1'

# from doctest import run_docstring_examples
# def largest_factor(x):
#     """Return the largest factor of x that is smaller than x.

#     >>> largest_factor(15) # factors are 1, 3, 5
#     5
#     >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
#     40
#     >>> largest_factor(13) # factor is 1 since 13 is prime
#     1
#     """
#     "*** YOUR CODE HERE ***"
#     # divisor = x - 1
#     for n in range(x - 1, 0, -1):
#         if (x % n == 0):
#             return n
#     return x
# run_docstring_examples(largest_factor, globals(), True)

def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    # if odd, multiply by 3 and add 1
    # if even, divide by 2
    # x = x
    while True:
        print(x)

        if x == 1:
            break
        elif x % 2 == 0:
            x //= 2
        else:
            x = (x * 3) + 1

hailstone(10)