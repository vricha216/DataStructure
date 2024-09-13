# def find_pairs_with_sum(array, target_sum):
#     """
#         Function to find two numbers in the list that add up to the target.
        
#         :param nums: List of integers
#         :param target: Target sum
#         :return: Tuple of two integers that add up to target
        
#         Time Complexity: O(n)
#         Space Complexity: O(n)
#     """
    
#     num_count = {}
#     pairs = []
    
#     for num in array:
#         complement = target_sum - num
#         if complement in num_count and num_count.get(complement,0) > 0 and num_count.get(num,0) > 0:
#             pairs.append((complement, num))
#             num_count[complement] -= 1
#             num_count[num] -= 1
#         else:
#             num_count[num] = num_count.get(num, 0) + 1
#             num_count[complement] = num_count.get(complement, 0) + 1
            
#     return pairs


def find_pairs_with_sum(arr,s):
    n = len(arr)
    h = {}
    pairs = []
    for i in arr:
        comp = s - i
        if comp in h and h.get(comp) > 0 and h.get(i)>0:
            pairs.append((comp,i))
            h[comp] -= 1
            h[i] -= 1
        else:
            h[i] = h.get(i,0) + 1
            h[comp] = h.get(comp,0)+1
    return pairs
         

def main():
    array1 = [10, 5, 2, 3, -6, 9, 11, -6]
    target_sum1 = 4
    result1 = find_pairs_with_sum(array1, target_sum1)
    print(f"Pairs with sum {target_sum1}: {result1}")  # Output: [(10, -6)]

    array2 = [1, 2, 3, 2]
    target_sum2 = 4
    result2 = find_pairs_with_sum(array2, target_sum2)
    print(f"Pairs with sum {target_sum2}: {result2}")  # Output: [(1,3),(2, 2)]

if __name__ == "__main__":
    main()
