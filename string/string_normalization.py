s = 'This is SO MUCH FUN!'
a = s.split(' ')
a = [word[0].upper() + word[1:] for word in a]
    
print(a)