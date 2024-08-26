# Implement a function that takes in two non-empty arrays of integers, finds the pair of numbers 
# (one from each array) who absolute difference is closest to zero, and returns a pair containing these two numbers, 
# with the first number from array.
# Only one such pair will exist for the test.




def get_min_diff(arr1,arr2):
    arr1.sort()
    arr2.sort()
    a = 0
    b = 0
    n = len(arr1)
    m = len(arr2)
    result = float('inf')
    best_pair = (None, None)

    while a<n and b<m:
        minn = abs(arr1[a]-arr2[b])
        if minn < result:
            result = minn
            best_pair = (arr1[a], arr2[b])
            
        if arr2[b]>arr1[a]:
            a+=1
        else:
            b+=1
            
    return best_pair
        
        
def main():
    arr1 = [23, 5, 10, 17, 30]
    arr2 = [26, 134, 135, 14, 19]
    print(get_min_diff(arr1,arr2))
    
if __name__ == "__main__":
    main()