class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = collections.deque()
        l, r = 0, len(nums)-1
        while(l<=r):
            left,right=abs(nums[l]),abs(nums[r])
            if left< right:
                ans.appendleft(nums[r]*nums[r])
                r-=1
            else:
                ans.appendleft(nums[l]*nums[l])
                l+=1
        return list(ans)






       

        






      
        
 

        