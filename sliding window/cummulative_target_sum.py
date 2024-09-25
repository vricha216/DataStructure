

#cummulative sum equals to target
#brute force
def brute_add_sum(a, k):
    n = len(a)
    if n < 1:
        return []
    i = 0
    s = 0
    ans = []
    while i<n:
        s = 0
        j = i
        while j<n and s<k:
            s+=a[j]
            if  s == k:
                ans.append((i,j))
            j+=1
        i+=1
    return ans

# #used to calculate prefix_sum
def get_prfx_sum(a,n):
    prfx_map = {}
    prfx_sum = 0
    for i in range(0,n):
        prfx_sum += a[i]  
        prfx_map[prfx_sum] = i 
    return prfx_map

def optim_add_sum(arr,k):
    n = len(arr)
    prfx_map = {0:-1}
    ans = []
    s = 0
    if n>1:
        print(prfx_map,"lol")
        for i in range(0,n):
            s += arr[i]
            if (s-k) in prfx_map:
                ans.append(((prfx_map.get(s-k)+1),i))
            prfx_map[s] = i
    return ans


#sliding window
def cumm_sum(plots,k):
    j = 0
    s = 0
    c = 0
    max_c = 0
    ans  = []
    n = len(plots)
    for i in range(0,n):
        s+=plots[i]
        while s>k and j<=i:
            s = s-plots[j]
            j+=1
            
        if s==k:
            max_c = max(max_c,c)
            l = i-j+1
            if l > c:
                c = l
                ans.append(plots[j:i + 1])
    return max_c,ans

# print(prfx[j] - prfx[i-1])
# sumofsubarray from idx i to j = prfx[j] - prfx[i-1]
# k = prfx[j] - prfx[i-1]
# prfx[i-1] = prfx[j] - k

# Approach
# iterate through the array and compute the prefix_sum and maintain a hash map for prefxx sum where key is sum and value is index
# calculate prfx sum and for each prfx sum , check if prfx-k has been seen in map or not 
# if seen append  pair prefx_map[(prfx sum - k)]+1 and i in to the answer
# if not seen just skip and maintain the prefix sum hash map


def main():
    # Case 1: Empty array
    plots = []
    k = 8
    print(optim_add_sum(plots, k))  # Expected output: []

    # Case 2: Single element equal to k
    plots = [8]
    k = 8
    print(optim_add_sum(plots, k))  # Expected output: [(0,0)]

    # Case 3: Single element greater than k
    plots = [10, 15, 20]
    k = 8
    print(optim_add_sum(plots, k))  # Expected output: []

    # Case 4: No subarray adds to k
    plots = [1, 2, 3]
    k = 10
    print(optim_add_sum(plots, k))  # Expected output: []

    # Case 5: Negative numbers
    plots = [1, 2, -1, 4, 5]
    k = 5
    print(brute_add_sum(plots, k))  # Expected output: [(1,3), (4,4)]

    # Case 6: Multiple subarrays of the same length
    plots = [4, 4, 4, 4]
    k = 8
    print(optim_add_sum(plots, k))  # Expected output: [(0,1), (1,2), (2,3)]

    # Case 7: All elements equal to k
    plots = [8, 8, 8]
    k = 8
    print(optim_add_sum(plots, k))  # Expected output: [(0,0), (1,1), (2,2)]

    # # # Case 8: Larger subarrays
    # plots = [3, 4, 1, 2, 5]
    # k = 9
    # print(optim_add_sum(plots, k))  # Expected output: [(1,4)]

if __name__ == '__main__':
    main()


# 1,3            1+3 = 4 < 8  i= 0,j=1
# 1,3,2          4+2 = 6 < 8  i= 0,j=2
# 1,3,2,1        6+1 = 7 < 8   i= 0,j=3
# 1,3,2,1,4      7+4 = 11 > 8   #sum = 0     i= 1,j=4


# (increament i) 3,2,1,4        3+2 = 5
# silicon valley