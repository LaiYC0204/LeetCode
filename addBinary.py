def funAddBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    a = int(a, 2)
    b = int(b, 2)
    return bin(a + b)[2:]

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    length = max(len(a), len(b))
    a = a.zfill(length)
    b = b.zfill(length)
    carry = 0
    output = ''
    for i in range(length - 1, -1, -1):
        if a[i] == '1' and b[i] == '1':
            if carry == 0:
                output = '0' + output
            elif carry == 1:
                output = '1' + output
            carry = 1
        elif a[i] == '1' or b[i] == '1':
            if carry == 0:
                output = '1' + output
                carry = 0
            elif carry == 1:
                output = '0' + output
                carry = 1
        else: # a[i] = 0 b[i] = 0
            if carry == 0:
                output = '0' + output
            elif carry == 1:
                output = '1' + output
            carry = 0
    if carry == 1:
        output = '1' + output
    return output

print(addBinary('1010', '1011'))