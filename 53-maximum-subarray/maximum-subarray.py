class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #current sum which we take each time
        cur_sum=0
        # max sum will be first assigned with 1 st value
        max_sum=nums[0]
        #then iterate 
        for i in range(len(nums)):
            #add each values one by one
            cur_sum+=nums[i]
            #check if cur sum is greater than max sum
            if cur_sum>max_sum:
                #if yes assign that to max_sum to max sum
                max_sum=cur_sum
            #if cur sum is negative will asign 0    
            if cur_sum<0:
                cur_sum=0
        return max_sum            

        