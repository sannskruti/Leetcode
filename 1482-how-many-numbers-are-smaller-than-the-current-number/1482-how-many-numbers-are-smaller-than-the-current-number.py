class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp=sorted(nums)
        res=[]
        myMap={}
        for i,num in enumerate(temp):
            if num not in myMap:
                myMap[num]=i
        for i in range (0, len(nums)):
            res.append(myMap[nums[i]])
        return res
            


      

       


       
            



       





        