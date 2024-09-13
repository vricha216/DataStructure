#brute force -> o(n**3)
#pairsum -> o(N*N) 

# 1. sort -> nlogn
# 2. iterate -> (a[i] o(n), (a[j],a[k]) pairsum(2 pointers)) -> o(n**2)



# nlogn+n**2 = n**2
def partition(arr,low,high):
    
    pivot = arr[high] #choosing last eleemnt as pivot
    i = low - 1
    for j in range(low,high):
        if arr[j]< pivot:
            i += 1 #move the pointer for smaller elements
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


def triplet_sum(arr:list,target:int):
    
    
    n = len(arr)
    quick_sort(arr,0,n-1)
    result = []
    for i in range(0,n-2):
        print("test")
        j = i+1
        k = n-1
        # In the worst case, for each fixed i, the range between j and k starts at n - i - 1.
        while j<=k:
            print("ytest2")
            curr_sum = arr[i]
            curr_sum += arr[j]
            curr_sum += arr[k]
            
            if curr_sum == target:
                result.append((arr[i],arr[j],arr[k]))
                j+=1
                k-=1
            elif curr_sum > target:
                k-=1
            else:
                j+=1
    return result
            

# def triplet_sum(arr:list,target:int):
#     arr.sort()
#     n = len(arr)
#     result = []
#     for i in range(0,n-2):
#         j = i+1
#         k = n-1
#         #two pointer approach
#         while j<k:
#             curr_sum = arr[i]
#             curr_sum += arr[j]
#             curr_sum += arr[k]
            
#             if curr_sum == target:
#                 result.append((arr[i],arr[j],arr[k]))
#                 j+=1
#                 k-=1
#             elif curr_sum>target:
#                 k-=1
#             else:
#                 j+=1
#     return result

def main():
    arr = [2,3,7,1,6,8,15,9,4,5]
    target = 18
    print(triplet_sum(arr,target))
    
if __name__ == "__main__":
    main()
    