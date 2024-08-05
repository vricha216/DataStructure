def matchingStrings(stringList, queries):
    x = {}
    ans = []
    for i in stringList:
        x[i] = x.get(i,0)+1
        
    for i in queries:
        ans.append(x.get(i,0))

    
    return ans


stringList = ['ab','ab','abc']
queries = ['ab','abc','bc']
print(matchingStrings(stringList, queries))

#output: [2,1,0]
