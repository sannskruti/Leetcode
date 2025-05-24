class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        print(nums)
        if not nums:
            return nums
        
        if nums[0]>0:
            return [i**2 for i in nums]
        if nums[-1] < 0:
            return [i**2 for i in nums][::-1]
        m=0

        for i in range(0, len(nums)):
            if nums[i]>=0:
                m=i
                break
            
        # split using m
        pos=nums[m:]
        neg=nums[0:m]
        print(pos,neg,m)
        neg.reverse()
        a,b=0,0
        ret=[]
        for i in range(0, len(pos)):
            pos[i]=pos[i]*pos[i]

        for i in range(0, len(neg)):
            neg[i]=neg[i]*neg[i]
        print(neg)
        
        while (a<len(pos) and b<len(neg)):
            if (neg[b])<(pos[a]):
                ret.append(neg[b])
                b+=1
            else:
                ret.append(pos[a])
                a+=1

        while(a<len(pos)):
            ret.append(pos[a])
            a+=1

        while (b<len(neg)):
            ret.append(neg[b])
            b+=1

        return ret

     
       

        






      
        
 

        