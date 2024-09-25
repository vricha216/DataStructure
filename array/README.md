# Arrays Problems

## Problem 1: Two Sum

### Problem Statement
Given an array of integers `nums` and an integer `target`, return distinct pair of numbers such that they add up to `target`.

### Possible Approaches
- **Brute Force Approach**: 

    - Description: Use two nested loops to check every pair of numbers in the array.
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    - Explanation: This approach checks all possible pairs to find the target sum. It’s simple but inefficient for large arrays due to the quadratic time complexity.
    
    
- **Hash Map Approach (Optimal Solution)**:

    - Description: Use a hash map (dictionary) to store the difference between the target and each element as we iterate through the array.
    - **Time Complexity**: O(n)
    - **Space Complexity:** O(n)
    - Explanation: As we traverse the array, we check if the complement of the current element (i.e., target - num) is already in the hash map. If it is, we have found our pair. If not, we add the current element to the hash map.
    
- **Sorting and Two-Pointer Approach**:
    - Description: First, sort the array. Then, use two pointers to find the two numbers that sum up to the target.
    - Time Complexity: O(n log n) due to the sorting step, plus O(n) for the two-pointer scan.
    - Space Complexity: O(1) (excluding the space used for sorting if in-place).
    - Explanation: After sorting, one pointer starts at the beginning and the other at the end of the array. Adjust the pointers based on the sum of the elements they point to. This approach is efficient but requires sorting.




<!-- // Question 2:
// The overall time complexity of the following code is ___________.

// for(int i= 0; i < n; i = i + j){
//      for( j = 0; j < k; j ++){
//        // some work
//      } 
// } -->

<!-- 
The following binary when stored in signed integer would represent ______________ ?

11111111111111111111111111111111 -->