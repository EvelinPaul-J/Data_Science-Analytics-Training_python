names = ['Anu', 'Arun', 'Bala', 'Banu', 'Cathy', 'Asha']
result = {}
for name in names:
    key = name[0].upper()
    if key not in result:
        result[key] = []
    result[key].append(name)
print(result)
