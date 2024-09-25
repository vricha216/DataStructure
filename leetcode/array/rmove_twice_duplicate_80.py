class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        k = n
        j = 2
        for i in range(2,n):
            if nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j+=1
        return j
    
    
    
nums = [1,1,1,2,2,3]
x = Solution()
x.removeDuplicates(nums)