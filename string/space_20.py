#WAF to replace all spaces in a string with %20.
#sameple I/p "hello world how are you?"
#o/p hello%20world%20how%20are%20you

def replace_chr(str):
    n = len(str)
    count_sp = str.count(' ')

    new_length = n + 2*count_sp
    k = ['']*new_length

    j = new_length - 1
    for i in range(n-1,-1,-1):
        if str[i] == ' ':
            k[j] = '0'
            k[j-1] = '2'
            k[j-2] = '%'
            j-=3
        else:
            k[j] = str[i]
            j-=1
    
    return ''.join(k)
    
str = "hello world how are you?"
print(str.split(' '))
print(replace_chr(str))