

def bubble_sort(arr,n):

    i = 0
    # i: Current pass number, starting from 0. It represents how many elements have already been sorted at the end of the list.

    while i<n-1:
        is_swapped = False
        j = 0
        while j<n-i-1:
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                is_swapped  = True
            j+=1
        if not is_swapped:
            break
        i+=1
    return arr

def main():
    array = [64, 25, 12, 22, 11]
    target_sum1 = 5
    result1 = bubble_sort(array, target_sum1)
    print(f"Pairs with sum {target_sum1}: {result1}")  # Output: [(10, -6)]
    

if __name__ == "__main__":
    main()
    


