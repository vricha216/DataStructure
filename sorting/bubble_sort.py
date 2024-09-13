

# def bubble_sort(arr,n):

#     i = 0
#     # i: Current pass number, starting from 0. It represents how many elements have already been sorted at the end of the list.

#     while i<n-1:
#         is_swapped = False
#         j = 0
#         while j<n-i-1:
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#                 is_swapped  = True
#             j+=1
#         if not is_swapped:
#             break
#         i+=1
#     return arr

def bubble_sort(arr,n):
    for i in range(0,n):
        swap = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        if not swap:
            break
    return arr

def main():
    array = [64, 25, 12, 22, 11]
    target_sum1 = 5
    result1 = bubble_sort(array, target_sum1)
    print(f"Pairs with sum {target_sum1}: {result1}")  # Output: [(10, -6)]
    

if __name__ == "__main__":
    main()
    

            

# Repeatedly swapping the adjacent element if they are in the wrong order
#first pass
# 64, 25, 12, 22, 11
# 64,25 ->  25, 64, 12, 22, 11
# 64,12 ->  25, 12, 64, 22, 11
# 64,22 ->  25, 12, 22, 64, 11
# 64,11 ->  25, 12, 22, 11, 64


# Algorithm
# traverse the array and compare the adjacent element and swap them if the right one is higher
# largest eleemnt will move to the rightmost end at first
# continur the first step to find the 2nd, 3rd untill the data becomes sorted



# Total Comparisons Calculation:
# for first pass it takes n-1 comparisons
# for 2nd pass it takes n-2 comparison
# for 3rd pass it takes n-2  comparison
# and so on
#for last we need 1 comparison

#Total no. of comparisons = (n-1)+(n-2)+(n-3)+...+1
# Total no. of comparisons: n*(n-1)/2


#advantage
# doesnt require any extra memory space
# Maintains relative order(stable)

#Applications
# usefull where we need to swap only adjacent elements(like in computer graphics to detect a tiny error in almost sorted arrays)
# Polygon filling algorithm

# Time Complexity: o(n**2) -> avg and worst case
#o(n) for already sorted(best case)


    
    


    


