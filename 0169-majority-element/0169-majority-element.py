class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {}
        res = majority = 0
        
        for n in nums:
            hash[n] = 1 + hash.get(n, 0)
            if hash[n] > majority:
                res = n
                majority = hash[n]
        
        return res
        