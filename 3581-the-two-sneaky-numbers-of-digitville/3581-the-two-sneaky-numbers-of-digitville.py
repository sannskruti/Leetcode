class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        mySet=set()
        res=[]


        for i in range (0, len(nums)):
            if nums[i] not in mySet:
                mySet.add(nums[i])
            else:
                res.append(nums[i])
        return res

        