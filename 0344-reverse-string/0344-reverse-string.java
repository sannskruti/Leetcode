class Solution {
    public void reverseString(char[] s) {
        int x= s.length-1;
        int i=0;
        while (i<x){
            char t='t';
            t=s[i];
            s[i]=s[x];
            s[x]=t;
            x=x-1;
            i=i+1;
        }
        return ;
    
    }
}