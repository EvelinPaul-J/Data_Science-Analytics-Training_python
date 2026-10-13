nums = [1, 1, 1]
k = 2
count = 0
prefix = 0
freq = {0: 1}
for num in nums:
    prefix += num
    count += freq.get(prefix - k, 0)
    freq[prefix] = freq.get(prefix, 0) + 1
print("Count:", count)
