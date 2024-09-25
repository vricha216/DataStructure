
    
#brute force
# def arr_prod(arr):
#     n = len(arr)
#     prod_arr = [1]*n
#     for i in range(0,n):
#         prod = 1
#         for j in range(0,n):
#             if j == i:
#                 continue
#             else:
#                 prod*=arr[j]
#         prod_arr[i] = prod
        
        
#     print(prod_arr)

def arr_prod(nums):
    n = len(nums)
    ans = [1]*n

    lt = 1
    rt = 1

    for i in range(0,n):
        ans[i] = lt
        lt *= nums[i]
    print(ans)

    for i in range(n-1, -1, -1):
        ans[i] = ans[i]*rt
        rt *= nums[i]

    return ans
    


nums = [1,2,3,4,5]


print(arr_prod(nums))
# nums = [0,0]
# print(arr_prod(nums))
# nums = [0,4,0]
# print(arr_prod(nums))
# nums = [0,4,1]
# print(arr_prod(nums))
# https://leetcode.com/problems/product-of-array-except-self/submissions/


# Compute the product of elements to the left of each index.
# Compute the product of elements to the right of each index.
# compute the product of elements to the right and multiply with the left products.
