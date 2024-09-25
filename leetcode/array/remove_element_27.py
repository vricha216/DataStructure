class Solution:
    def removeElement(self, nums, val: int) -> int:
        n = len(nums)
        k = 0
        for i in range(0,n):
     
            if nums[i] != val:
                nums[k],nums[i] = nums[i],nums[k]
                k+=1
            
        return k
    
    
obj = Solution()
nums ,val = [3,2,2,3] ,3
obj.removeElement(nums,val)
# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150