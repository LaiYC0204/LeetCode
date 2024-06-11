def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    sign = 1
    i = 0

    #1.檢查前導空白字元
    while i < len(s) and s[i] == ' ':
        i += 1

    #2.檢查符號(- +)
    if i < len(s) and (s[i] == '-' or s[i] == '+'):
        if s[i] == '-':
            sign = -1
        i += 1

    #3.確認是否在0~9中
    output = 0
    for string in s[i:]:
        if string.isdigit(): 
            output = output * 10 + int(string)
        else: 
            break

    #4.確認目前數字大小
    output *= sign
    if output > 2**31 - 1: 
        return 2**31 - 1
    elif output < -2**31:
        return -2**31

    return output

answers = {'42':42, ' -042':-42, '1337c0d3':1337, '0-1':0, 'words and 987':0, '-91283472332':-2147483648, '+1':1, '-+12':0, '.1':0}
#answers = {'.1':0}

for key, value in answers.items():
    output = myAtoi(key)
    if output != value:
        print(f'Key: {key}, Value: {value}, Output: {output}')