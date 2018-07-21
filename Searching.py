def search(inpL, number):
    for index in range(len(inpL)):
        if number == inpL[index]:
            return index
        
    return -1

print(search(range(0, 200000000), 56458796))






def Factorial():
    if n == 0: 
        return 1
    elif n == 1:
        return 1
    else 