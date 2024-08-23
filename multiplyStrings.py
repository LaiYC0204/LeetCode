def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    output = 0
    
    for posI, i in enumerate(range(len(num1) - 1, -1, -1)):
        for posJ, j in enumerate(range(len(num2) - 1, -1, -1)):
            output += int(num1[i]) * int(num2[j]) * (10 ** (posI + posJ))

    return str(output)

def GPTmultiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    # 初始化结果数组，长度是两个数长度之和
    result = [0] * (len(num1) + len(num2))

    # 逐位相乘
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            # 结果的当前位置
            pos1, pos2 = i + j, i + j + 1
            # 累加到当前位置
            temp_sum = mul + result[pos2]

            # 处理进位
            result[pos2] = temp_sum % 10
            result[pos1] += temp_sum // 10

    # 去除结果前导零并转化为字符串
    result_str = ''.join(map(str, result)).lstrip('0')
    return result_str if result_str else "0"

print(multiply('123', '456'))

