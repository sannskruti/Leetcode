class Solution:
    def reverse(self, x: int) -> int:
        xCopy=x
        x=abs(x)
        rev=0
        while (x>0):
            rem=x%10
            rev= 10*rev+rem
            x=x//10

        limit= math.pow(2,31)
        if rev < -limit or rev>limit:
            return 0
        if xCopy <0:
            return -rev
        else:
            return rev
