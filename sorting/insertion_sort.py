

def insertion_sort(arr,n):
    
    for i in range(1,n):
        j = i-1
        k = arr[i]
        while j>=0 and k<arr[j]:
            arr[j+1] = arr[j]
            print(arr)
            j-=1
        
        arr[j+1] = k
            
    return arr    


def main():
    array = [64, 25, 12, 22, 11]
    n = 5
    arr = insertion_sort(array, n)
    print(f"sorted array :{arr}")
    
if __name__ == "__main__":
    main()
    
# divide the array into parts sorted and un-sorted then pick a value from unsorted array and placed it to the sorted array


#Algorithm
#           [64, 25, 12, 22, 11]
#         /                    \
# [64](supposed sorted)       [25, 12, 22, 11](unsorted)
# /                                 \
# [25,64]                          [12, 22, 11]
# (compare first 
# element from 
# unsorted and swap
# if it is smaller)
# / 
# [25,]





