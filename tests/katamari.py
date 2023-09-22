

# insert modes:
# i -> insert at cursor (insert)
# a -> add space on insert (append)
# o -> add newline after cursor
# I -> insert at beginning of line 
# O -> add newline before cursor
# A -> insert at end of line (append)



def aggregate(fn, seq, pred):
    """
    >>> def is_even(x):
            return x % 2 == 0
    >>> def sum_plus_one(x, y):
            return x + y + 1
    """
    result = None
    true_values = [x for x in seq if pred(x)]

    if len(true_values) > 1:
        result = seq[0]
        for idx in range(0, len(seq) - 1):
            result = fn(result, seq[idx + 1])
    if len(true_values) == 1:
        result = true_values[0]
    return result



def is_even(x):
    return x % 2 == 0

def sum_plus_one(x, y):
    return x + y + 1

# tests = []
# test 1
# expected = 14
# result = aggregate(sum_plus_one, [2, 4, 6], is_even)
# tests.append(expected == result) 

# # test 2
# expected = None
# result = aggregate(sum_plus_one, [1, 3, 5, 7, 9], is_even)
# tests.append(expected == result) 

# # test 3
# expected = 2
# result = aggregate(sum_plus_one, [1, 2, 3], is_even)
# tests.append(expected == result)

# # test 4
# expected = 23
# result = aggregate(sum_plus_one, [2, 4, 6, 8], is_even)
# tests.append(expected == result) 

from operator import add, mul

fact = lambda x: aggregate(mul, [x for x in range(1, x+1)], lambda x: x >= 0) if x > 0 else 1

# Test 5
expected = 1
result = fact(0)
assert expected == result 

# Test 6
expected = 120
result = fact(5)
assert expected == result 
