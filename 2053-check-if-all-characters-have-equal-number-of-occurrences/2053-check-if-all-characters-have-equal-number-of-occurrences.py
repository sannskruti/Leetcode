class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s_map={}
        for i in range (0, len(s)):
            if s[i] in s_map:
                s_map[s[i]]+=1
            else:
                s_map[s[i]]=1
        print(s_map)
        
        for key in s_map:
            if s_map[key]!=s_map[s[0]]:
                return False
        return True
            


        