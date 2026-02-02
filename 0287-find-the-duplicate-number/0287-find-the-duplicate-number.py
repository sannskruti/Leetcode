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







 