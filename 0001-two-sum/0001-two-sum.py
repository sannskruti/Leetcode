class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff=0
        numMap={}
        for i,n in enumerate(nums):
            diff= target-nums[i]
            if diff in numMap:
                return [numMap[diff],i]
            else:
                numMap[n]=i









      

        