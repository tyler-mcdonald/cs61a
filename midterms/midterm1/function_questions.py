########################################################################################################################
# fall 2015 midterm 1
####################################### Q3(a)
def find_digit(n, d):
    """
    >>> find_digit(567, 7)
    0
    >>> find_digit(567, 5)
    2
    """
    i, k = 0, False
    while n:
        n, last = n // 10, n % 10
        if last == d:
            k = i
        i = i + 1
    return k

assert find_digit(567, 7) == 0
assert find_digit(567, 5) == 2
assert find_digit(567, 9) == False
"""
3 Lessons
- When dealing with numbers, don't cross into string territory. Find the solution in math.
- When there is greater than 1 solution type (e.g. integer or boolean), use control to reassign, instead of multiple
return statements (just a rule of thumb)
- While statements are preferred unless a simple loop is involved.
"""


####################################### Q3(c)
def luhn_sum(n):
    """
    >>> luhn_sum(135)       # 1 + 6 + 5
    12
    >>> luhn_sum(185)       # 1 + (1+6) + 5
    13
    >>> luhn_sum(138743)    # 2 + 3 + (1+6) + 7 + 8 + 3
    30
    """
    # if digit*2 < 10:
    #   return digit
    # else:
    #   return the sum of each digit in digit*2
    def luhn_digit(digit):
        # multiplier is 1 or 2 
        x = digit * multiplier
        # 16 // 10 == 1     4 // 10 == 0
        # 16 % 10 == 6      4 % 10 == 4
        # add these together
        return (x // 10) + x % 10
    total, multiplier = 0, 1
    while n:
        # traverse backwards through n by removing last digit
        n, last = n // 10, n % 10
        # add luhn_digit to total
        total = total + luhn_digit(last)
        # cycle between 1 and 2 to calculate luhn_digit
        multiplier = 3 - multiplier
    return total

assert luhn_sum(135) == 12
assert luhn_sum(185) == 13
assert luhn_sum(138743) == 30
"""
Lessons
- Traverse backwards through any number with x // 10 and x % 10
- x // 10 gets the first part of the number (325 // 10 == 32) and (325 / 10 == 32.5)
- x % 10 gets the remainder or last digit (325 % 10 == 5) because (325 / 10 == 32.5). It's getting the 0.5.
- Cycle between even and odd with (3 - 1 == 2) and (3 - 2 == 1) -> easy way to get even/odd positions.
"""


####################################### Q3(d)
def check_digit(n):
    """
    >>> check_digit(153)    # 2 + 5 + 6 + 7 = 20
    1537
    """
    # if luhn_sum(n) % 10 != 0
    #   find digit that makes  


assert check_digit(153) == 1537
assert check_digit(13874) == 138743



########################################################################################################################





