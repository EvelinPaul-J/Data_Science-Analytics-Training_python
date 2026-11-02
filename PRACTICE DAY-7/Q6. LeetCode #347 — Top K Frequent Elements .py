'''Q6. LeetCode #347 — Top K Frequent Elements 
Problem Statement: Given a list of numeric measurements and an integer k,
 return the k most frequent values. This resembles identifying the most common error codes or sensor 
 readings in a dataset. Implement top_k_frequent(nums, k). The answer may be returned in any order; 
 do not use collections.Counter.
Example Input: nums = [1, 1, 1, 2, 2, 3]
k = 2
Example Output: Top 2 frequent values: [1, 2] (order may vary)'''
def top_k_frequent(nums, k):
    frequency={}
    for n in nums:
        if n in frequency:
            frequency[n]= frequency[n]+1
        else:
            frequency[n]=1
    result =sorted(frequency, key=frequency.get, reverse=True)
    return result[:k]
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))