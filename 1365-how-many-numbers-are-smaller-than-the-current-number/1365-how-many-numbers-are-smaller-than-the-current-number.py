class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # sorted_nums=sorted(nums)
        # freq_dict={}

        # for i, num in enumerate(sorted_nums):
        #     if num not in freq_dict:
        #         freq_dict[num]=i
        # ans=[]
        # for num in nums:
        #     ans.append(freq_dict[num])

        # return ans


        count_array=[0]*101
        # [0,1,2,1,0,0,0,0,1]
        prefix_sum=[0]*101
        res=[]

        for num in nums:
            count_array[num]+=1
        # print('count:',count_array)
        
        for i in range(0,101):
            prefix_sum[i]=prefix_sum[i-1]+ count_array[i]
        # print('prefix:', prefix_sum)

        for i in range (0, len(nums)):
            res.append(prefix_sum[nums[i]]-count_array[nums[i]])

        # print("res:",res)

        return res

        


        







        
        