class Solution {
public:
    int maxSubArray(vector<int>& nums) {
    
    int sum=0;
    int maxsum=INT_MIN;
        for(int i=0;i<nums.size();i++){
            sum+=nums[i];
            maxsum=max(maxsum,sum);
            if(sum<0) sum=0;            
        }
        return maxsum;   
    
    
    
    
    
    
    
    //     if(nums.size()==1) return nums[0];
    //    int sum=0;
    //    int maxsum =INT_MIN;
    //    for(int i=0;i<nums.size();i++){
    //         sum+=nums[i];           
    //         maxsum = max(maxsum, sum);
    //         if(sum<0) sum=0;
    //    }
       
    //    return maxsum;
       
       /* int maxsum= INT_MIN;
        int sum=0;
        for(int i =0;i<nums.size();i++){
            for(int j=i;j<nums.size();j++){
             sum +=nums[j];
             if(sum>maxsum){
                maxsum=sum;
            }
            }
            sum=0;
            
        }
        return maxsum;*/
    }
};