class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_map={}
        t_map={}
        if len(s)!=len(t):
            return False
        for i in range (0, len(s)):
            if  s[i] in s_map:
                s_map[s[i]]+=1
            else:
                s_map[s[i]]=1
            if t[i] in t_map:
                t_map[t[i]]+=1
            else:
                t_map[t[i]]=1
        print (s_map)
        print (t_map)
        if s_map==t_map:
            return True
        else:
            return False
     
           

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


        
        

      
       





        