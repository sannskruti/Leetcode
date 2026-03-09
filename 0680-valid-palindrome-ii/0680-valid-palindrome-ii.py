class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s is None:
            return

        l=0
        r=len(s)-1

        def checkSubString(l,r):
            while(l<r):
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
            
        while(l<r):
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return checkSubString(l+1,r) or checkSubString(l,r-1)
        return True
        