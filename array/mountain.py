
def highest_mountain(arr):
    maxx = 0
    n = len(arr)
    peak = None
    i = 0
    while i<=n-2:
        #check if a[i] is the peak or not
        if arr[i-1] < arr[i] > arr[i+1]:
            count = 1
            back_step = i
            #count backwd(left)
            while back_step>=1 and arr[back_step]> arr[back_step-1]:
                back_step-=1
                count+=1
            #count fwd(right)
            while i<=n-2 and arr[i]>arr[i+1]:
                i+=1
                count+=1  
                
            maxx = max(maxx,count)
        else:
            i+=1
        
    return maxx


arr = [5,6,1,2,3,4,5,4,3,2,0,1,2,3,-2,4]

maxx = highest_mountain(arr)
print(maxx)

    