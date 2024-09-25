a= [1,9,3,0,18,5,2,4,10,7,12,6]

# largestband = [0,1,2,3,4,5,6,7]
# n = len(a)
# a.sort()
# ans = []
# for i in range(0,n-2):
#     if a[i+1]-a[i] > 1:
#         ans.append(i)
#         break
# print(a[:ans[0]])


def largest_band(a):
    n = len(a)
    i = 0
    # j = 1
    cnt = 0
    #to find start
    while i<n:
        if a[n]-1 not in a:
            start = a[n]

        i+=1
        while start:
            start = start+1
            if start in a:
                cnt+=1
                
# (element) 5
# /           \
# element-1     6
#                 \            
#                   7(and so on)
            
        
