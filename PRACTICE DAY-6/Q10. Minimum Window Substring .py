s = 'ADOBECODEBANC'
t = 'ABC'
need = {}
for c in t:
    need[c] = need.get(c, 0) + 1
left = 0
missing = len(t)
start = 0
min_len = float('inf')
for right in range(len(s)):
    c = s[right]
    if c in need:
        if need[c] > 0:
            missing -= 1
        need[c] -= 1
    while missing == 0:
        if right - left + 1 < min_len:
            start = left
            min_len = right - left + 1
        ch = s[left]
        if ch in need:
            need[ch] += 1
            if need[ch] > 0:
                missing += 1
        left += 1
if min_len == float('inf'):
    print("Minimum window:", '')
else:
    print("Minimum window:", repr(s[start:start + min_len]))
