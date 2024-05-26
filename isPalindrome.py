#我寫的
def myIsPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    for i in range(len(x)):
        if x[i] != x[len(x) - 1  - i]:
            return False
    return True

#跟我寫的依樣 更便捷的寫法
def mySimpleIsPalindrome(x):
    numStr = str(x)
    return numStr == numStr[::-1]

#數字顛倒
def otherIsPalindrome(x):
    if x < 0:
        return False
    temp = x
    reverse = 0
    while temp != 0:
        reverse = reverse * 10 + temp % 10
        temp //= 10

    return x == reverse

answers = {121:True, -121:False, 10:False}
for key, value in answers.items():
    output = mySimpleIsPalindrome(key)
    if output != value:
        print(f'Key: {key}, Value: {value}, Output: {output}')