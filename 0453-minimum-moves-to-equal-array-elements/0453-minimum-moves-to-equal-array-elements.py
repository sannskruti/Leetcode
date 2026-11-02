class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_element=min(nums)
        operations=0

        for i in range (0,len(nums)):
            operations+=nums[i]-min_element

        return operations


        