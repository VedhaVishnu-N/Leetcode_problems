"""
the solution i provided before failed at test cases here is the new solution provided below for the problem
class Solution(object):
    def removeElement(self, nums, val):
        count=0
        l=0
        n=len(nums)-1
        while l<n:
            if nums[l]==val:
                while nums[n]==val: 
                    n-=1
                nums[l],nums[n]=nums[n],nums[l]
                count+=1
            l+=1
        return (len(nums)-1-count)
"""

class Solution(object):
    def removeElement(self, nums, val):
        i=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i
