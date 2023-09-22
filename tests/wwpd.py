def f(x):
    return not x

def my_pow(x, n):
    print(x, n)
    if f(n):
        return 1
    elif n < 0:
        return 1 // my_pow(x, -n)
    elif n % 2:
        return x * my_pow(x, n - 1)
    return my_pow(x * x, n // 2)

def hero(spider):
    def man(home):
        def marvel(home):
            return None
        print(spider)
        print(marvel)
        return spider - home
    return man

goat = lambda m: lambda n: m - n
bleat = (lambda a, b, c, d: b or a(d)(c))(goat, 5 == 6, 7, 4)
