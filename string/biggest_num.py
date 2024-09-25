# You are given a array of numbers. You want to concatenate these numbers together to form the 
# lexicographically largest number. Print that largest number number. 
# You can't rearrange the digits of any number, however you can place the numbers next to each other in any order.

# Input
# 10,11,20,30,3

# Output
# 330201110 
from functools import cmp_to_key
def comparator(a,b):
    if a + b > b + a:
        return 1
    elif a + b < b + a:
        return -1
    else:
        return 0    

def largest_num(a: list):
    a = list(map(str,a))
    a.sort(key=cmp_to_key(comparator),reverse=True)
    print(a)
    return ''.join(a)

a = [10,11,20,30,3]
ans = largest_num(a)

print(ans)