class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        myset=set(nums)
        for i in range (1,n+1):
            if i not in myset:
                res.append(i)   
        return res
            
                

            



        