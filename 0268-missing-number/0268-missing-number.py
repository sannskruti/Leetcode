class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        myset=set(nums)
        for i in range (0,n+1):
            if i not in myset:
                return i
            myset.add(i)
            
        