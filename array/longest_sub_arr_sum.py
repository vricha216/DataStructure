# Example 1:
# Input Format: N = 3, k = 5, array[] = {2,3,5}
# Result: 2
# Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.

# Example 2:
# Input Format: N = 5, k = 10, array[] = {2,3,5,1,9}
# Result: 3
# Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.



# 2
# 2,3
# 2,3,5
# 2,3,5,1
# 2,3,5,1,9
# 3
# 3,5
# 3,5,1
# 3,5,1,9

# 5
# 5,1
# 5,1,9

# 1
# 1,9

#brute force O(n**3)
# def largest_sub_arr_sum(arr,k,n):
#     s = 0
#     l = 0
#     for i in range(0,n): 
#         for j in range(i+1,n):
#             s =sum(arr[i:j+1])
#             if s == k:
#                 l = max(l,j-i+1)
                
#     print(l)

#brute force  O(n**2)
# def largest_sub_arr_sum(arr,k,n):
#     s = 0
#     l = 0
#     for i in range(0,n): 
#         s  = 0
#         for j in range(i+1,n):
#             s += arr[j]
#             if s == k:
#                 l = max(l,j-i+1)
                
#     print(l)
    
    
#using hashing
def largest_sub_arr_sum(arr,k,n):
    m = {}
    n = len(arr)
    max_len = 0
    pref_s = 0
    for i in range(0,n):
        pref_s+=arr[i]
        
        if pref_s == k:
            max_len = max(max_len, i+1)
            
        rems = pref_s - k
        if rems in m:
            l = i - m[rems]
            max_len = max(max_len,l)
        m[pref_s] = i
    return max_len
        

#using 2 pointers
# class Solution:
#     def lenOfLongSubarr (self, arr, n, k) : 
#         left = 0
#         max_l = 0
#         curr_sum = 0
#         right = 0
#         while right < n:
#             curr_sum += arr[right]
#             while left<=right and curr_sum>k:
#                 curr_sum = curr_sum - arr[left]
#                 left+=1
#             if curr_sum == k:
#                 max_l = max(max_l, right-left+1)
            
#             right+=1
#             # if right<n: curr_sum += arr[right]

#         return max_l

           
# 2
# 2,3
# 2,3,5
# 2,3,5,1,9 

# 10+5+2 = 17

arr = [2,3,5,1,9]
k = 10
n = 5
# ob = Solution()

print(largest_sub_arr_sum(arr,n,k))

# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/description/
# https://leetcode.com/problems/count-almost-equal-pairs-i/
# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/