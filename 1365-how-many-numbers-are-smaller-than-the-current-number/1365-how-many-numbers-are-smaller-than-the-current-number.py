class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums=sorted(nums)
        freq_dict={}

        for i, num in enumerate(sorted_nums):
            if num not in freq_dict:
                freq_dict[num]=i
        ans=[]
        for num in nums:
            ans.append(freq_dict[num])

        return ans




        
        