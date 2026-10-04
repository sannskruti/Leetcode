class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet=set(nums)
        max_len=0

        for num in numSet:
            if num-1 not in numSet:
                current_num=num
                length=0

                while current_num in numSet:
                    length+=1
                    current_num+=1
                max_len=max(max_len,length)
        return max_len
                


   










        