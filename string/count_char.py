# Sample Inputs

# bbbaaaadexxxxxx
# abc
# Sample Outputs

# b3a4d1e1x6
# abc


def count_char(s):
    """
    if we dont need to maintqain the consecutive order
    like I/P = "abaac"
    O/P should be a3bc
    """
    a = {}
    m = ''
    for i in s:
        a[i] = a.get(i,0)+1
    
    for i in a:
        m = m+i+str(a[i])
    return m

def count_Char(s):
    """
    if we need to maintqain the consecutive order
    like I/P = "abaac"
    O/P should be a1b1a2c
    """
    m = ''
    n = len(s)
    c = 0
    for i in range(1,n):
        print(s[i],s[i-1])
        if s[i] == s[i-1]:
            c+=1
              
        else:
            m = m+s[i-1]+str(c+1)
            c = 0
            
    m = m + s[-1] + str(c + 1)
            
            
    print(m)



s = 'bbbaaaadexxxxxx'
print(count_Char(s))
s = 'abcad'
print(count_Char(s))
