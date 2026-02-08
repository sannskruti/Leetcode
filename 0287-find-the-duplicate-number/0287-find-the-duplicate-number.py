class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [1,3,4,2,2]
        # output=2


        mySet=set()
        for num in nums:
            if num not in mySet:
                mySet.add(num)
            else:
                return num


        # slow=0
        # fast=0
        # while (fast < len(nums)):
        #     if nums[slow]==nums[fast]:
        #         return nums[slow]
        #     else:
        #         slow=nums[slow]
        #         fast=nums[nums[fast]]

        
        # for i in range (len(nums)):
        #     num = nums[i]
        #     while num != nums[num-1]:
        #         old = nums[num - 1]
        #         nums[num-1] = num
        #         num = old
        # print(nums)
        # return nums[len(nums) - 1]

    
      
        
        
        

        

        






       


   




  
