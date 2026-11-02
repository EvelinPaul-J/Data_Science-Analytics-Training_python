'''Q5. LeetCode #49 — Group Anagrams 
Problem Statement: Given a list of strings representing category labels, group strings that are anagrams of one another. Return a list of groups. The order of groups does not matter, but strings within each group should preserve their input order. Implement the solution as a function group_anagrams(strs). This is useful for grouping normalized labels or tokens by character composition.
Example Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Example Output: Groups (group order may vary):
['eat', 'tea', 'ate']
['tan', 'nat']
['bat']'''
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
def group_anagrams(strs):
    grp = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key not in grp:
            grp[key] = []
        grp[key].append(s)
    print(list(grp.values()))
group_anagrams(strs)

