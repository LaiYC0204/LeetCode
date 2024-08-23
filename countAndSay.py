def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    output = '1'
    for _ in range(2, n + 1):
        currentCount = 0
        tempOutput = ''
        currentNum = output[0]
        for currentOutput in output:
            if currentOutput == currentNum:
                currentCount += 1
            else:
                tempOutput += str(currentCount) + currentNum
                currentNum = currentOutput
                currentCount = 1
        tempOutput += str(currentCount) + currentNum
        output = tempOutput

    return output

print(countAndSay(10))