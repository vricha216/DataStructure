# Implement a function that takes an input an array of integers, and prints the maximum 
# subarray sum that can be formed. A subarray is defined as consecutive segment of the array. 
# If all numbers are negative, then return 0.



def max_subarray_sum(arr):
    n = len(arr)
    max_sum = 0
    cur_sum = 0
    for i in range(0,n):
        cur_sum+=arr[i]
        max_sum = max(max_sum,cur_sum)
        if cur_sum<0:
            cur_sum = 0

    return max_sum

# cur_sum = -1
# max_sum = -1

# cur_sum = -1+2 =1
# max_sum = (-1,1) = 1

# cur_sum  = 1+3 = 4
# max_sum = (1,4) = 4

# cur_sum = 4+4 = 8
# max_sum = (8,4) = 8


# cur_sum = 8-2 = 6 
# max_sum = (8,6) = 8

# cur_sum = 6-6 = 0 
# max_sum = (8,0) = 8


def main():
    arr = [-1,2,3,4,-2,6,-8,3]
    print(max_subarray_sum(arr))
    

if __name__ == "__main__":
    main()
