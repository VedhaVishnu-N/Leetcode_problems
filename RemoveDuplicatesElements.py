class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        arr=[]
        for j in range(len(nums)):
            if nums[j] not in arr:
                nums[i]=nums[j] 
                i+=1
            arr.append(nums[j])
        return i
        
# Here is an modified version of Removing Duplicate Element from sorted array with reduced Complexity 
class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        val=None
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
            val=nums[j]
        return i
        