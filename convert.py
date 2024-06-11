def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s

    output = ''
    rows = ['' for _ in range(numRows)]
    i = 0
    check = True
    for word in s:
        rows[i] += word
        if check:
            i += 1
        else:
            i -= 1

        if i == 0:
            check = True
        elif i == numRows-1:
            check = False

    for row in rows:
        output += row
    return output


#想法一模一樣，寫法不一樣
def otherconvert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    curr_row = 0
    going_down = False

    for char in s:
        rows[curr_row] += char
        if curr_row == 0 or curr_row == numRows - 1:
            going_down = not going_down
        curr_row += 1 if going_down else -1

    return ''.join(rows)

answers = {'PINALSIGYAHRPI':['PAYPALISHIRING', 4], 'PAHNAPLSIIGYIR':['PAYPALISHIRING', 3], 'A':['A', 1], 'aaaaabbbbb':['ababababab', 2], 'AB':['AB', 1]}

for key, value in answers.items():
    output = convert(value[0], value[1])
    if output != key:
        print(f'Key: {value}, Value: {key}, Output: {output}')


"""
P     I     N
A   L S   I G
Y A   H R
P     I
"""