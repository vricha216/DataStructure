#find the sortest subarray that needs to be sorted in place so that entire array become sorted
#if the input array is already sorted,the fucntion should return [-1,-1],otherwise return the start and end index of smallest subarray



# arr = [1,2,3,4,5,8,6,7,9,10,11]
# sorted_arr = [1,2,3,4,5,6,7,8,9,10,11]
# i = 0
# j = 10
# take 2 pointers one on starting and another one on end
# increament i if we got the element which is not matched from forward
# decremant j if we got the element which is not matched from backward
# output = [5,7] (indexes)



#brute force -> o(nlogn)
# def sort_subarr(arr):
#     #sort the array
#     n = len(arr)
#     b = sorted(arr)
#     i = 0
#     j = n-1
#     while i<n and arr[i] == b[i]:
#         i+=1
#     while j>0 and arr[j] == b[j]:
#         j-=1
    
#     if i == n:
#         return [-1,-1]
#     return [i,j]


def get_start(arr,start_in,n):
    for i in range(0,n-1):
        if arr[i+1]-arr[i] != 1:
            start_in = i+1
            return start_in
    return -1
    
            
def get_end(arr,start_in,end_in,n):
    if start_in == -1:
        return -1
    for i in range(start_in,n-1):
        if arr[i+1]-arr[i] == 1:       
            end_in = i+1
            return end_in
    return n-1

def sort(arr):
    n = len(arr)
    start_in = -1
    end_in = -1
    start_in = get_start(arr,start_in,n)
    end_in = get_end(arr,start_in,end_in,n)
    
    return [start_in,end_in]



a1 = [1, 3, 5, 4, 2, 6, 8, 7, 9, 10]
print(sort(a1))

# needs to sort -> [8,6,7]
#range 5-7
# s = 0
# arr[i+1] - arr[i] = 1
# if t!=1:
#     s = i


# Before sorting: [1, 3, 5, 4, 2, 6, 8, 7, 9, 10]
# After sorting: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Unsorted segments: [(1, 4), (6, 7)]