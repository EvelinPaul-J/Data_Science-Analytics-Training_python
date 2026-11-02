'''Q1. LeetCode #238 — Product of Array Except Self (Medium)
Problem Statement: Given a list of integers nums, return a list answer such that answer[i] equals the
 product of all elements of nums except nums[i]. Do not use division. Aim for O(n) time.
   Implement the solution as product_except_self(nums). This problem is useful for practicing efficient 
   transformations over numerical datasets.
Example Input: nums = [1, 2, 3, 4]
Example Output: Product array: [24, 12, 8, 6]'''
#nums = [1, 2, 3, 4]
#for i in nums:
def product_except_self(nums):
    ans=[]
    for i in range(len(nums)):
        value=1
        for j in range(len(nums)):
            if i != j:
                value = value * nums[j]
        ans.append(value)
    return ans
nums = [1, 2, 3, 4] 
print  (product_except_self(nums))