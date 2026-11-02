'''Q3. Variable-Length Positional Arguments with *args
Problem Statement: Implement average_readings(*args). Return the average of any number of numeric readings.
 Return None if no readings are supplied.
Example Input: average_readings(10, 20, 30, 40)
average_readings()
Example Output: Average: 25.0
No readings provided'''
def average_readings(*args):
    if len(args) == 0:
        return None
    total=sum(args)
    count=len(args)
    average=total / count
    return average
print(average_readings(10, 20, 30, 40))
print(average_readings())