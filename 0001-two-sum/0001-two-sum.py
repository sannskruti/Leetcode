class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict={}
        for i in range (0, len(nums)):
            diff=target-nums[i]
            if diff in myDict:
                return [i, myDict[diff]]
            myDict[nums[i]]=i

# I need to store key value pairs in my dict , which would be nums[i] as key and its index from num as value





        