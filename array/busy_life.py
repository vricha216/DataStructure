
# Select the maximum number of activities such that no two activities overlap.

# Approach:
# Sort the activities by their finish times.
# Select the first activity (the one with the earliest finish time).
# for each activity check if current activity time is greater than the last one 
# if yes append the value and update previous activity time and continue


def busy_life(arr):
    n = len(arr)
    arr.sort(key = lambda x : x[1])
    summ = 0
    ans = [arr[0]]

    #previos selected activity
    prev_activity_time = arr[0][1]
    for i in range(1,n):
        curr_activity_time = arr[i][0]
        print(curr_activity_time,prev_activity_time)
        if curr_activity_time>= prev_activity_time:
            ans.append(arr[i])
            prev_activity_time = arr[i][1]
        
    return ans


arr = [(7,9), (0,10), (4,5), (8,9), (4,10), (5,7)]
print(busy_life(arr))
# o/p = 3([(4,5),(5,7),(7,9)])



# [(7,9), (0,10), (4,5), (8,9), (4,10), (5,7)]

# 1-5: Date with crush (end at 5) -> i=0

# 2-5: Watch a movie (end at 5) -> i=1


# 1-7: Coding contest (end at 7) -> cant pick -> i=2

# 6-9: Play DotA (end at 9) -> i=3

# 8-11: Study (end at 11)  -> cant pick -> i=4
 
# 9-12: Sleep (end at 12) -> i=5

# idx_ar = [0,2,3,]

# [ [ 4, 5 ], [ 5, 7 ], [ 7, 9 ], [ 8, 9 ], [ 0, 10 ], [ 4, 10 ] ]

# [ 4, 5 ], [ 5, 7 ], [ 7, 9 ]