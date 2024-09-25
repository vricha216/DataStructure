


#approach
#we can decide if the number we choose could be start of band or not for this we can check if (curr number - 1) is present in list or not
#if present this can not be head
# we can create a loopkup table(unordered set) for looking the elements in O(1)


def max_band(arr):
    count = 0
    final_count = 0
    x = set(arr)
    
    for i in arr:
        if (i-1) not in x:
            start = i
            count = 1
            while start+1 in x:
                count+=1
                start+=1
            final_count = max(count,final_count)
            
    return final_count
                

def main():
    arr = [1,9,3,0,18,5,2,4,10,7,12,6]
    output = 8
    print(max_band(arr))
    
if __name__ == '__main__':
    main()