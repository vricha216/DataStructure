def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotateLeft(d, arr):
    n = len(arr)
    d %= n  # In case d > n
    reverse(arr, 0, n-1)       # Reverse the entire array
    reverse(arr, 0, n-d-1)     # Reverse the first part (n-d elements)
    reverse(arr, n-d, n-1)     # Reverse the second part (last d elements)
    return arr

d = 4
arr = [1, 2, 3, 4, 5]
rotated_array = rotateLeft(d, arr)
print(rotated_array)