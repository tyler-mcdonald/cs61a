"""Trees."""

from notes.tree import *

t = tree(1, [tree(2), tree(4)])

# label(t)
# 1
# No abstraction barriers were broken.

# t[0]
# 1
# This breaks the abstraction barrier, because it assumes that the tree was
# implemented using a list.

# label(branches(t)[0])
# 2
# This is not in violation of abstraction, because it's given in the description
# of the ADT (abstract data type) that the return value of branches() returns a list

# is_leaf(t[1:][1])
# Evaluates to True
# This violates an abrstraction barrier, because it assumes the implementation
# of branches(t). Although branches() returns a list, this assumes that the
# implementation of branches() is itself a list, which is the violation of the
# abstraction. The specific part in violation here it t[1:], which is breaking
# the abstraction barrier put in places by the branches() function. The second
# part [1] is NOT in violation of abstraction since we know that branches()
# itself returns a list. A better implementatio of this code is: is_leaf(branches(t)[1])

# [label(b) for b in branches(t)]
# [2, 4]
# This doesn't violate any barriers.

# branches(tree(5, [t, tree(3)]))[0][0]
# tree: [5, [[1, [2, 4]], 3]]
# Evaluates to 1
# This breaks an abstraction barrier because it assumes the tree is built using
# a list, given that the second [0] is trying to access the label element of the
# first branch. The first [0] is fine, because we know that branches() returns a
# list, but the second [0] selector violates the abstraction.
# An equivalent expression which doesn't break abstraction barriers is:
#   label(branches(tree(5, [t, tree(3)]))[0])


def height(t: tree):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    if is_leaf(t):
        return 0
    else:
        return max([height(b) + 1 for b in branches(t)])


def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    else:
        return max([max_path_sum(b) + label(t) for b in branches(t)])


def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t) == x:
        return [label(t)]
    for b in branches(t):
        path = find_path(b, x)
        if path:
            return [label(t)] + path


def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    >>> t = tree(10, [tree(20, [tree(0)]), tree(5), tree(5)])
    >>> sum_tree(t)
    40
    """
    return sum([label(t)] + [sum_tree(b) for b in branches(t)])


def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    return not any(
        [
            sum_tree(branches(t)[0]) != sum_tree(b) or not balanced(b)
            for b in branches(t)
        ]
    )