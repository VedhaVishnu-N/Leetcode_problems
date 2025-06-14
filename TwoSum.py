def twoSum(self, nums, target):
    for i in nums:
        for j in nums[i:]:
            if i+j==9:
                return [i,j]
                
