'''Q10. LeetCode #28 — Find the Index of the First Occurrence in a String
Problem Statement: Implement str_str(haystack, needle), returning the index of the first occurrence of
 needle in haystack, or -1 if needle does not occur. If needle is an empty string, return 0. Do not use 
 the built-in find() or index() methods.
Example Input: haystack = "datascience"
needle = "science"
Example Output: First occurrence index: 4
'''
haystack="datascience"
needle="science"
if needle=="":
    print("First occurrence index: 0")
else:
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)]==needle:
            print("First occurrence index:", i)
            break
    else:
        print("First occurrence index: -1")