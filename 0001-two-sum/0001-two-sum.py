class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        smap={}
        for i in range (0, len(nums)):
            diff=target-nums[i]
            if diff in smap:
                return [smap[diff],i]
            smap[nums[i]]=i



        
