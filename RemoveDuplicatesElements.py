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
        