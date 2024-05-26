def myRomanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} 
    output = 0
    s_length = len(s) - 1
    while s_length >= 0:
        if((s[s_length] == 'M' or s[s_length] == 'D') and s[s_length-1] == 'C' and s_length-1 >= 0):
            output += roman[s[s_length]] - roman['C']
            s_length -= 2
        elif((s[s_length] == 'L' or s[s_length] == 'C') and s[s_length-1] == 'X' and s_length-1 >= 0):
            output += roman[s[s_length]] - roman['X']
            s_length -= 2
        elif((s[s_length] == 'V' or s[s_length] == 'X') and s[s_length-1] == 'I' and s_length-1 >= 0):
            output += roman[s[s_length]] - roman['I']
            s_length -= 2
        else:
            output += roman[s[s_length]]
            s_length -= 1
    return output

"""別人寫的執行速度最快，我修改一下
如果不是最後一位字母
    如果前者數字比當前數字大或等於那麼sum += 當前數字
    如果前者數字比當前數字小那麼sum -= 當前數字
如果是最後一位字母
    sum += 當前數字
"""
def otherRomanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} 
    sum = roman[s[-1]]
    for i in range(len(s)-1,0,-1):
        if roman[s[i-1]] >= roman[s[i]]:
            sum = sum + roman[s[i-1]]
        else:
            sum = sum - roman[s[i-1]]
    return sum

answers = {'MCMXCIV':1994, 'LVIII':58, 'III':3, 'MMMCDXC':3490, 'IV':4}

for key, value in answers.items():
    output = otherRomanToInt(key)
    if output != value:
        print(f'Key: {key}, Value: {value}, Output: {output}')