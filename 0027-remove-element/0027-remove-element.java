class Solution {
    public int removeElement(int[] nums, int val) {
        int x=0;
        int n=nums.length;

        for(int i=0;i<n;i++){
            if (nums[i] != val){
                nums[x]=nums[i];
                x=x+1;
            }
            
        }  
        return x;  
    }
}