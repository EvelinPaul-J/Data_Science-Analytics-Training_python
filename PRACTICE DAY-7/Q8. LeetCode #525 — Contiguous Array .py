'''Q8. LeetCode #525 — Contiguous Array 
Problem Statement: Given a binary list, find the maximum length of a contiguous subarray containing an 
equal number of 0s and 1s. This can model balanced binary outcomes in a sequence of observations. 
Implement find_max_length(nums) in O(n) time using a prefix-sum balance and dictionary.
Example Input: nums = [0, 1, 0]
Example Output: Maximum balanced subarray length: 2'''
def find_max_length(nums):
    balance=0
    length=0
    dict={0:-1}
    for i in range(len(nums)):
        if nums[i]==0:
            balance=balance-1
        else:
            balance=balance+1
        if balance in dict:
            length = max(length, i - dict[balance])
        else:
             dict[balance] = i
    return length    
nums = [0, 1, 0]
print("Maximum balanced subarray length:", find_max_length(nums))

