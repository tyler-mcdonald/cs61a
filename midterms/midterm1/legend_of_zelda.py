empty = 'empty'

def link(first, rest=empty):
    return [first, rest]

def first(lnk):
    return lnk[0]

def rest(lnk):
    return lnk[1]

def linked_sum(lnk, total):
    """
    >>> # Four combinations: 1 1 1 1 , 1 1 2 , 1 3 , 2 2
    >>> linked_sum(link(1, link(2, link(3, link(5)))), 4)
    4
    """
    if total == 0:
        return 1
    elif lnk == empty or total < 0:
        return 0
    else:
        with_first = linked_sum(lnk, total - first(lnk))
        without_first = linked_sum(rest(lnk), total)
        return with_first + without_first

result = linked_sum(link(1, link(2, link(3, link(5)))), 4)
