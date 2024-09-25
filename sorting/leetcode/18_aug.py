
10101
def countKConstraintSubstrings(s: str, k: int) -> int:
    l = 0 
    n = len(s)
    x = [0,0]
    count = 0
    for r in range(0,n):
        x[int(s[r])] += 1
        print(x)
        while x[0] > k and x[1] > k:
            x[int(s[l])] -= 1
            l += 1
        count += (r - l + 1)
        
    return count
            
            
# You are given a binary string s and an integer k.
# A binary string satisfies the k-constraint if either of the following conditions holds:
# The number of 0's in the string is at most k.
# The number of 1's in the string is at most k.
# Return an integer denoting the number of substrings of s that satisfy the k-constraint.

# Example 1:
# Input: s = "10101", k = 1
# Output: 12
s = "10101"
k = 1
countKConstraintSubstrings(s, k)
# Explanation:
# Every substring of s except the substrings "1010", "10101", and "0101" satisfies the k-constraint.