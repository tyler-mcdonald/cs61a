






a = [
        {"total": 10, "inactive": 10},
        {"total": 5, "inactive": 10},
        {"total": 99, "inactive": 10},
        {"total": 200, "inactive": 10},
        {"total": 40, "inactive": 500}
]

b = sorted(a, key=lambda x: x['total'] - x['inactive'])

print(b)