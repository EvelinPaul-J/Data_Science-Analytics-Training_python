sales = {
    'Sensor': [4, 6, 5],
    'Cable': [10, 2, 3],
    'Board': [8, 7],
    'LED': [5, 5, 5]
}
totals = {}
for product, values in sales.items():
    totals[product] = sum(values)
result = sorted(totals.items(), key=lambda x: (-x[1], x[0]))
for product, total in result:
    print(f"{product}: {total}")
