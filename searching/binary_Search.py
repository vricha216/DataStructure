# useful for sorted array only
# access to any element of the data structure shoukd take constant time
# need to divide the search interval untill the target value found


# algorithm
# divide the array into 2 halves
# compare the middle element of the search space with the key 
# if key is found loop terminated
# if key is not found at middle:
    # if key is smaller than the middle, search for right side
    # if larger than the middle, search for left side
    
#the process is continued untill the key is found or all elements are traversed

def binary_search(arr, start, end, target):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        # if target is greater ignore left half
        elif arr[mid] < target:
            start = mid + 1
         # if target is smaller ignore right half
        else:
            end = mid - 1
    return -1
        


arr = [2,3,4,10,40,15]
x = 10
print(binary_search(arr, 0, len(arr)-1, x))

