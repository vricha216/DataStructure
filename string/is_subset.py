#check subsets
# need to check if s2 is subset of s1 or not

def is_subset(s1,s2):
    i = len(s1)-1
    j = len(s2)-1

    while i>=0 and j>=0:
        if s1[i] == s2[j]:
            j-=1
        i-=1

    return j == -1


s1 = "coding minutes"
s2 = "cines"      
ans = is_subset(s1,s2)
print(ans)