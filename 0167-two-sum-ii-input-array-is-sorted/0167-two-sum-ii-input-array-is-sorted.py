class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        myDict={}
        for i in range (0, len(numbers)):
            diff=target-numbers[i]
            if diff in myDict:
                return [myDict[diff]+1, i+1]
            myDict[numbers[i]]=i
           

        