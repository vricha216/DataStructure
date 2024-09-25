#it works on divide and conquer approach

# Algorithm
# divide the list or array into 2 halves untill it is divisible
# sort the each subarray individually
# merge these sorted array 
# continues till elements from both subarrays have been merged


# Time Complexity:
# Best Case: O(n log n), When the array is already sorted or nearly sorted.
# Average Case: O(n log n), When the array is randomly ordered.
# Worst Case: O(n log n), When the array is sorted in reverse order.

#38 27 43 10
#    /    \
# 38,27   43,10
#   /\      / \
# 38  27   43  10
#   \/       \/
# 27,38     10,43

# Advantages of Merge Sort:
#stable: mainatin the relative order of elements

#disadvantage
#not in place(space complexity)


def sort_and_merge(left,right):
    print(left,right,"right")
    merged_arr = []
    i = j = 0
    while i< len(left) and j<len(right):
        if left[i] < right[j]:
            merged_arr.append(left[i])
            i+=1
        else:
            merged_arr.append(right[j])
            j+=1
    print(left[i:],right[j:],i,j)
    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])
    return merged_arr

def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    mid = n//2
    left = arr[0:mid]
    right = arr[mid:]
    return sort_and_merge(merge_sort(left),merge_sort(right))
    


arr = [9,6,2,9,1]
arr = [1,5,3,4,2,6]
merge_sort(arr)