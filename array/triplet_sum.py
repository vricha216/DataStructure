#brute force -> o(n**3)
#pairsum -> o(N*N) 

# 1. sort -> nlogn
# 2. iterate -> (a[i] o(n), (a[j],a[k]) pairsum(2 pointers)) -> o(n**2)


# nlogn+n**2 = n**2
[2,3,7,1,6,8,15,9,4,5]

curr_sum = 2
curr_sum = 2+3 = 5
curr_sum = 5+5 = 10


def triplet_sum(arr:list,target:int):
    arr.sort()
    n = len(arr)
    result = []
    for i in range(0,n-2):
        j = i+1
        k = n-1
        #two pointer approach
        while j<k:
            curr_sum = arr[i]
            curr_sum += arr[j]
            curr_sum += arr[k]
            
            if curr_sum == target:
                result.append((arr[i],arr[j],arr[k]))
                j+=1
                k-=1
            elif curr_sum>target:
                k-=1
            else:
                j+=1
    return result

def main():
    arr = [2,3,7,1,6,8,15,9,4,5]
    target = 18
    print(triplet_sum(arr,target))
    
if __name__ == "__main__":
    main()
    