#it is based on divide and conquer
#Algortithmß
# Choose a pivot
# Partition the array around pivot
  #Elements smaller than the pivot are placed to its left.
  #Elements greater than the pivot are placed to its right.
# After partitioning, the pivot is in its final sorted position.


# Initial Array:   [10, 80, 30, 90, 40, 50, 70]
# Pick Pivot (70): [10, 30, 40, 50, 70, 90, 80]
# Left Subarray:   [10, 30, 40, 50]    Right Subarray: [90, 80]
# Sorted Left:     [10, 30, 40, 50]    Sorted Right:   [80, 90]
# Final Sorted:    [10, 30, 40, 50, 70, 80, 90]


def partition(arr,low,high):
    
    pivot = arr[high] #choosing last eleemnt as pivot
    i = low - 1
    for j in range(low,high):
        if arr[j]< pivot:
            i += 1 #move the pointer for smaller elements
            print(i,j,arr,"lol")
            arr[i], arr[j] = arr[j],arr[i]
            
    # place the pivot element in its correct position
    arr[i+1],arr[high] = arr[high],arr[i+1]
    print(arr)
    return i+1 #return the partitioning index

def quick_sort(arr,low,high):
    if low>high:
        return
    
    pi = partition(arr,low,high)
    quick_sort(arr, low, pi - 1)
    quick_sort(arr, pi + 1, high)
    
    


def main():
    array = [2,3,7,1,6,8,15,9,4,5]
    n = len(array)
    low = 0
    high = n -1
    result1 = quick_sort(array,low,high)
    print(f"sorted array {array}") 
    

if __name__ == "__main__":
    main()