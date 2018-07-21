def sortL(inpL):
    if len(inpL) <= 1:
        return inpL
        
    for i in range(1, len(inpL)):
        key = inpL[i]
        j = i - 1
        
        while j >= 0 and inpL[j] > key:
           inpL[j + 1] = inpL[j]
           j -= 1
           
        inpL[j + 1] = key
        
    return inpL
    
print (sortL([1, 10000, 5, 4, -1, 1, 1, 2, 100, 10]))
        




