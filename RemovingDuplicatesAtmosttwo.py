class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        val=None
        count=0
        for j in range(len(nums)):
            if nums[j]!=val:
                count=0
            if count<2 or nums[j]!=val:
                nums[i]=nums[j]
                i+=1
                count+=1
            val=nums[j]
        return i
        