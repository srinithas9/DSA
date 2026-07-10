class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # psum=[0 for i in range(len(nums))]
        # sum=0
        # for i in range(len(nums)):
        #     sum=sum+nums[i]
        #     psum[i]=sum
        # return psum  
        ans=[]
        ans.append(nums[0])  
        for i in range(1,len(nums)):
            x=ans[i-1]+nums[i]
            ans.append(x)
        return ans    
