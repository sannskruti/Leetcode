class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        new=[]
        for num in nums:
            heapq.heappush(new,num)
            if len(new) > k:
                heapq.heappop(new)
        return new[0]

# nums = [3,2,3,1,2,4,5,5,6], k = 4

# [3,2,3,1,2]

# [3,2,3,2,4]

# [3,3,2,4,5]

# [3,3,4,5,5]

# [3,4,5,5,6]

# [3]

# 4

            
        