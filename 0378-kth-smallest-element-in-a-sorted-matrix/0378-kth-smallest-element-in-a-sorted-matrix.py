class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n= len(matrix)
        heap=[]
        #Step 1: push first element of each row
        for r in range(n):
            heapq.heappush(heap,(matrix[r][0],r,0))

        # Step 2: pop k times
        for _ in range(k):
            value,r,c=heapq.heappop(heap)


            # Step3: push next element in the same row
            if c+1<n:
                heapq.heappush(heap,(matrix[r][c+1],r,c+1))

        return value
        