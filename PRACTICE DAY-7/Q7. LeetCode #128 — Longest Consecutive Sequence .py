'''Q7. LeetCode #128 — Longest Consecutive Sequence 
Problem Statement: Given an unsorted list of integer IDs or measurements, return the length of the longest 
consecutive-value sequence. The sequence values need not be adjacent in the input list. 
Aim for O(n) time using a set. Implement longest_consecutive(nums).
Example Input: nums = [100, 4, 200, 1, 3, 2]
Example Output: Longest consecutive sequence length: 4
Sequence: 1, 2, 3, 4'''
def longest_consecutive(nums):
    s=set(nums)
    long= 0
    sequence_list=[]
    for n in s:
        if n-1 not in s:
            current=n
            count=1
            sequence=[current]
            while current+1 in s:
                current=current+1
                count=count+1
                sequence.append(current)
            if count > long:
                long=count
                sequence_list=sequence
    print("Sequence:",sequence_list)
    return long
nums = [100, 4, 200, 1, 3, 2]
print("Longest consecutive sequence length:", longest_consecutive(nums))