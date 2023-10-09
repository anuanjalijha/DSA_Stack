def countBracketReversals(inputString) :
    n = len(inputString)
    s = []
    if n%2!=0:
        return -1 
    for i in range(n):
        if inputString[i]=='{':
            s.append(inputString[i])
        elif inputString[i]=='}' and s:
            if s[-1]=='{':
                s.pop()
            else:
                s.append(inputString[i])
        else:
            s.append(inputString[i])

    count = 0
    while s:
        c1 = s.pop()
        c2 = s.pop()
        if c1==c2:
            count+=1
        else:
            count+=2

    return count                                        
