class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i = 0
        # j = 1
        # while j < len(nums):
        #     if nums[i] != nums[j]:
        #         nums[i+1] = nums[j]
        #         i = i + 1
        #     j = j + 1
        # return i + 1        
        start=0
        n=len(nums)
        for i in range(1,n):
            if nums[i]!=nums[start]:
                start+=1
                nums[start]=nums[i]
        return start+1    

        