def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sign = -1 if x < 0 else 1

    temp = x * sign
    output = 0
    while temp != 0:
        output = output * 10 + temp % 10
        temp //= 10

    if not (-2**31 <= output <= 2**31 -1):
        return 0

    return output * sign

answers = {123:321, -123:-321, 120:21, 1534236469:0}

for key, value in answers.items():
    output = reverse(key)
    if output != value:
        print(f'Key: {key}, Value: {value}, Output: {output}')