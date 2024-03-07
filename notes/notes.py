def fact_times(n, k):
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)


fact_times(4, 1)


def tree(label, branches):
    pass


t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
