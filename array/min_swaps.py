#miimum number of swaps required to swap the array
# 1. find correct location of each element(sorting - nlogn)
# 2. store the current indices

def min_swap(arr):
    arr_with_index = []
    n = len(arr)
    ans = 0
    visited = [False]*(n)   
    for i in range(0,n):
        arr_with_index.append((i,arr[i]))
        
    arr_with_index.sort(key=lambda x: x[1]) #sort the array containing tuple
    
    for i in range(0,n):
        
        #if element is visited or element is on right position
        old_pos = arr_with_index[i][0]
        if visited[i] or old_pos == i:
            continue

        #if element is visited first time
        curr_n = i
        cycle = 0
        while not visited[curr_n]:
            print("lol==")
            visited[curr_n] = True
            next_n = arr_with_index[curr_n][0] #move to the index of the next element in the cycle
            curr_n = next_n
            cycle+=1
        
           
        ans += cycle-1
    return ans
        
        
    
def main():
    # arr = [2,4,5,1,3]
    # print(min_swap(arr))
    arr = [5,4,3,2,1]
    print(min_swap(arr))
    # arr = [10,11,5,4,3,2,1]
    # print(min_swap(arr))

if __name__ == '__main__':
    main()


# Step-by-Step Execution:
# Initial Array:

# arr = [2, 4, 5, 1, 3]
# Pair Each Element with Its Index:

# We create pairs of (index, value) using enumerate:
# python
# Copy code
# arr_with_index = [(0, 2), (1, 4), (2, 5), (3, 1), (4, 3)]
# Sort Based on the Array Values:

# We sort arr_with_index based on the values:
# python
# Copy code
# arr_with_index.sort(key=lambda x: x[1])
# # After sorting: arr_with_index = [(3, 1), (0, 2), (4, 3), (1, 4), (2, 5)]
# This shows the correct position of each element.
# Initialize visited Array:

# visited = [False, False, False, False, False]
# Traverse the Sorted Array and Calculate Minimum Swaps:

# Cycle 1:
    # Start at index i = 0, arr_with_index[0] is (3, 1):
    # It's not visited, and it's not in the correct position (3 != 0).
    # Follow the cycle:
        # Move to index 3 (next_index = 3): (1, 4) → visited = [True, False, False, False, False]
        # Move to index 1 (next_index = 1): (0, 2) → visited = [True, False, False, True, False]
        # Move to index 0 (next_index = 0): (3, 1) → visited = [True, True, False, True, False]
        # Cycle length is 3, so cycle_size - 1 = 3 - 1 = 2 swaps are required.
# Cycle 2:
    # Move to index i = 1, but it's already visited, so skip.
# Cycle 3:
    # Move to index i = 2, arr_with_index[2] is (4, 3):
    # It's not visited, and it's not in the correct position (4 != 2).
    # Follow the cycle:
    # Move to index 4 (next_index = 4): (2, 5) → visited = [True, True, False, True, True]
    # Move to index 2 (next_index = 2): (4, 3) → visited = [True, True, True, True, True]
    # Cycle length is 2, so cycle_size - 1 = 2 - 1 = 1 swap is required.

