class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num=0
        if original in nums:
            num=original*2
            while num in nums:
                num=num*2
            return num
        else:
            return original


       

        