stock = {'LED': 20, 'RESISTOR': 50, 'SENSOR': 4}
requested = ['LED', 'SENSOR', 'SWITCH']
for item in requested:
    value = stock.get(item)
    if value is None:
        print(item + ": unavailable")
    else:
        print(f"{item}: {value} available")
