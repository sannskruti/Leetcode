class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqArr=[]
        for i in range (0, len(nums)):
            sqArr.append(nums[i] * nums[i])
        return sorted(sqArr)
        
 

        