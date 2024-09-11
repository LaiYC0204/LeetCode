# 記憶體不足的問題
def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1
    
    result = x
    for _ in range(abs(n) - 1):
        result *= x

    if n < 0:
        result = 1 / result

    return result

# 指數快速冪
def GPTmyPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1
    
    if n < 0:
        x = 1 / x
        n = -n
    
    result = 1
    current_product = x
    
    while n > 0:
        if n % 2 == 1:
            result *= current_product
        current_product *= current_product
        n //= 2
    
    return result


print(myPow(2.00000, -2))