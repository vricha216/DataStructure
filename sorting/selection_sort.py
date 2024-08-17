

def selection_sort(arr,n):
    i = 0
    j = i+1
    while i<=n-1:
        j = i+1
        min_idx = i
        while j<=n-1:
            if arr[j]<arr[min_idx]:
                min_idx = j
            j+=1
        arr[min_idx],arr[i] = arr[i],arr[min_idx]
        i+=1
                
    return arr

# Stable Selection Sort


def main():
    array = [64, 25, 12, 22, 11]
    n = 5
    result1 = selection_sort(array, n)
    print(f"sorted array {}: {result1}")  # Output: [(10, -6)]

if __name__ == "__main__":
    main()