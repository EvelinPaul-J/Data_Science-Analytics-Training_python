records = [
    ('D01', 'Lab-A', 'READY'),
    ('D02', 'Lab-B', 'BUSY'),
    ('D01', 'Lab-C', 'MAINTENANCE')
]
result = {}
for device, location, status in records:
    result[device] = {
        'location': location,
        'status': status
    }
print(result)
