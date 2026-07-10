# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         start=1
#         n=len(nums)
#         for i in range(2,n):
#             if nums[i]!=nums[start-1]:
#                 start+=1
#                 nums[start]=nums[i]
#         return start+1  
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return min(2, len(nums)) if len(nums) < 2 else k