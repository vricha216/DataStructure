#naive approach
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        m = len(strs)-1
        i = 0
        s = ''
        if m == 0:
            return strs[0]
        
        small = len(strs[m])
        if len(strs[0]) < len(strs[m]):
            small = len(strs[0])

        while i<small:
            if strs[0][i] != strs[m][i]:
                return s
                
            s+=strs[0][i]
            i+=1
            
        return s
    
#optimized
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

strs = ["flower","flow","flight"]
x = Solution()
x.longestCommonPrefix(strs)

# https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150