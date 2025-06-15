class Solution(object):
    def rotate(self, nums, k):
        arr=[]
        k=k%len(nums)
        arr=nums[-k:]+nums[:-k]
        for i in range(len(nums)):
            nums[i]=arr[i]