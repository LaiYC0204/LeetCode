def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    # dividend = 27, divisor = 3
    output = 0

    # 被除數為0 回傳0
    if dividend == 0:
        return 0
    
    # 被除數為最小數除視為-1 結果會溢出 輸出最大數整數
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1

    # 確認結果符號 正或負
    negative = False
    if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0):
        negative = True

    # 轉換成正數比較好運算
    dividend = abs(dividend)
    divisor = abs(divisor)

    while dividend >= divisor:
        temp_divisor = 0
        displacement = 0
        # 位移找到最大倍數 3 << 3 = 24 小於 27
        while temp_divisor <= dividend:
            displacement += 1
            temp_divisor = divisor << displacement

        displacement -= 1
        # 被除數減去最大倍數 dividend = 27 - 24 = 3
        dividend -= divisor << displacement
        # 答案增加1的位移數次方 output = 1 << 3 = 8
        output += 1 << displacement
    
    if negative:
        return -output
    return output
        
inputs = [[10,3], [7,-3],[27,3]]
answers = [3,-2,9]

for length in range(len(inputs)):
    output = divide(inputs[length][0], inputs[length][1])
    if answers[length] != output:
        print(f'input:{inputs[length]} output:{output} answer:{answers[length]}')