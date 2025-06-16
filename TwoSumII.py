class Solution(object):
    def twoSum(self, numbers, target):
        low=0
        high=len(numbers)-1
        while low<=high:
            total=numbers[low]+numbers[high]
            if total==target:
                return [low+1,high+1]
            elif total<target:
                low=low+1
            else:
                high=high-1

        