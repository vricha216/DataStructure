def selection_sort(arr,n):
    for i in range(0,n):
        minimum = i
        for j in range(i+1,n):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i],arr[minimum]= arr[minimum],arr[i]
    return arr


# [64, 25, 12, 22, 11]

# min = 12
# 12,25,64,22,11
# min = 22
# 12,22,64,25,11
# min = 22
# 12,22,64,25,11




# def selection_sort(arr,n):
#     i = 0
#     j = i+1
#     while i<=n-1:
#         j = i+1
#         min_idx = i
#         while j<=n-1:
#             if arr[j]<arr[min_idx]:
#                 min_idx = j
#             j+=1
#         arr[min_idx],arr[i] = arr[i],arr[min_idx]
#         i+=1
                
#     return arr

# Stable Selection Sort
def main():
    array = [64, 25, 12, 22, 11]
    n = 5
    result1 = selection_sort(array, n)
    print(f"sorted array {result1}") 
    
    


if __name__ == "__main__":
    main()
    
    
# Algorithm
# Traverse through all array elements
# Find the smallest element in the remaining part of the array
# Swap the minimum element with the first unsorted element


#Advantage
# simple and easy
# works well with small dataset
# IN place algorithm

# Disadvantage
# complexity O(n**2) for worst and average case
# doesnt preserve the relative order of items with equal keys i.e. not stable

# Applications
# works as basis for effecient algorithm like Heap Sort(uses heap data structure with selection sort base)
# used when memeory writes are costly


#Pending
# stable selection sort