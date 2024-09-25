
def is_palindrome(s: str,n: int):
    i = 0
    
    j = n-1
    while i < n and j>0:
        if s[i] == s[j]:
            i+=1
            j-=1
        else:
            return False
    return True

def palindrome_break(s: str):
    n = len(s)
    if n==1:
        return ""
    
    a = is_palindrome(s,n)
    if a:
        for i in range(0,n//2):
            if s[i]!='a':
                return s[:i]+'a'+s[i+1:]
        return s[:-1]+'b'
    else:
        return ""
            
    
        


s = "abccba"
ans = palindrome_break(s)
print(ans)
# output = "aaccba"

