class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        x = {}
        for i in nums:
            x[i] = x.get(i,0)+1
            if x.get(i) > n/2:
                return i
            
            
            
# Approach 3: Moore Voting Algorithm ->  To  discuss
nums = [3,2,3] #output 3
x = Solution()
x.removeDuplicates(nums)