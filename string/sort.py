

# input
# 3
# "92 022"
# "82 12"
# "77 13"
# 2 False numeric

# 2 means sort by 2nd  colunm  
# false/true -> reversed order or not
#numeric -> comparison should be numeric/lexicographical


#ouput
# "82 12" 
# "77 13"
# "92 022"

def sort_str(s,col,comparison_type,reversed):
    k = {}
    for i in s:
        strr = i.split(' ')
        k[strr[0]] = str(strr[1])
        
    sort_k = sorted(k.items(),key = lambda items: int(items[1]) )
    return sort_k

n = 3
s=[ "92 022","82 12","77 13"]
col = 2
reversed = False
comparison_type = 'numeric'
print(sort_str(s,col,comparison_type,reversed))