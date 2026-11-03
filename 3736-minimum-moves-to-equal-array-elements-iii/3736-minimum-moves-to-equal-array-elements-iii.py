class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num=max(nums)
        moves=0
        for i in range (0, len(nums)):
            moves+=max_num - nums[i]
        return moves


        
        