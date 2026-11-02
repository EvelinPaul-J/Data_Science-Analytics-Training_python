'''Q9. LeetCode #58 — Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
Example Input: s = "   Embedded Python   "
Example Output: Length of last word: 6
'''
def leng_of_lastword(s):
    result=s.split()
    return len(result[-1])
s = "   Embedded Python   "
print("Length of last word:",leng_of_lastword(s))