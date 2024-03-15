def ordered_digits(x):
    '''
assert ordered_digits(5) == True 
    >>> ordered_digits(11) 
    True 
    >>> ordered_digits(127) 
    True 
    >>> ordered_digits(1357) 
    True 
    >>> ordered_digits(21) 
    False
    '''
    # def next_to_last(n):
    while True:
        last = x % 10
        next_to_last = x // 10 % 10
        if next_to_last == 0:
            return True
        if last < next_to_last:
            return False
        x //= 10

assert ordered_digits(5) == True 
assert ordered_digits(11) == True 
assert ordered_digits(127) == True
assert ordered_digits(1357) == True 
assert ordered_digits(21) == False
