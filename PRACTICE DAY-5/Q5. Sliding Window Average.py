sales = [10, 20, 30, 40, 50, 60]
K = 3
averages = []
for i in range(len(sales) - K + 1):
    avg = sum(sales[i:i+K]) / K
    averages.append(round(avg, 2))
print("Window averages:", averages)
