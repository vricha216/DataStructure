#creating all substrings
#string should be sorted by length first and then in lexicographic order if length is same

def merge(a1,a2):
    n = len(a1)
    m = len(a2)
    i = 0
    j = 0
    merged_arr = []
    while i < n and j < m:
        if len(a1[i]) < len(a2[j]):
            merged_arr.append(a1[i])
            i+=1
        elif len(a1[i]) > len(a2[j]):
            merged_arr.append(a2[j])
            j+=1
        else:
            if a1[i] < a2[j]:
                merged_arr.append(a1[i])
                i+=1
            else:
                merged_arr.append(a2[j])
                j+=1
        
    merged_arr.extend(a1[i:])
    merged_arr.extend(a2[j:])
    return merged_arr

def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    mid = n//2
    return merge(merge_sort(arr[:mid]),merge_sort(arr[mid:]))
    
def generate_subsequences(s,i,o,subsequences):
    n = len(s)
    if n == i:
        subsequences.append(o)
        return
    
    generate_subsequences(s,i+1,o+s[i],subsequences)
    generate_subsequences(s,i+1,o,subsequences)

def get_sorted_subsequences(s):
    
    subsequences = []
    generate_subsequences(s,0, "", subsequences)
    subsequences = merge_sort(subsequences)    
    return subsequences

s = 'abcd'
subsequences = get_sorted_subsequences(s)
print(subsequences)