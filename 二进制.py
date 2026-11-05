def divideBy2(decNumber): 
    remstack = []
    while decNumber > 0:
        nums = decNumber % 2 
        remstack.append(nums)
        decNumber = decNumber//2
    binString = ""
    while len(remstack) > 0:
        binString = binString + str(remstack.pop())
    return binString
print(divideBy2(123))