# DATA STRUCTURE 1
# 1]Contains duplicates
##Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.##
#python

class Solution(object):
    def containsDuplicate(self, nums):
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)
                
#2]maximum subaarray
##Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.##      
#python3

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = []
        arr.append(nums[0])
        maxSum = arr[0]
        for i in range(1, len(nums)):
            arr.append(max(arr[i-1] + nums[i], nums[i]))
            if arr[i] > maxSum:
                maxSum = arr[i]
        return maxSum
                
