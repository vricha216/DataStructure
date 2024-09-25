class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        nums1_blank_space = m+n-1

        while i>=0 and j>=0:
            if nums1[i] > nums2[j]:
                nums1[nums1_blank_space] = nums1[i]
                i-=1
            else:
                nums1[nums1_blank_space] = nums2[j]
                j-=1
            nums1_blank_space-=1
        
        while j>=0:
            nums1[nums1_blank_space] = nums2[j]
            j-=1
            nums1_blank_space-=1

def main():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    obj = Solution()
    obj.merge(nums1,m,nums2,n)
    print(nums1) #expected: [1, 2, 2, 3, 5, 6]
    nums1,m,nums2,n = [1], 1,  [], 0
    obj.merge(nums1,m,nums2,n)
    print(nums1) #expected: [1]
    nums1,m,nums2,n = [0], 0, [1], 1
    obj.merge(nums1,m,nums2,n)
    print(nums1) #expected: [1]
    
if __name__ == '__main__':
    main()
        
        
#approach
# using 2 pointers both are at end one at end of nums1 and another one is at nums2 as both are sorted array
# as nums1 have extra space append the value at these places by comparing values with nums2

# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150