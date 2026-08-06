class Solution {
    public int removeDuplicates(int[] nums) {
        int n=nums.length;
        int x=0;
        for(int i=0;i<n;i++){
            
            if (nums[i]>nums[x]){
                x=x+1;
                nums[x]=nums[i];
            }
        }
        return (x+1);

        
    }
}