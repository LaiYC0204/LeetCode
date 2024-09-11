def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    result = []
    len_j, len_i = len(matrix), len(matrix[0])  # 注意，len_j 是行數，len_i 是列數
    top, bottom, left, right = 0, len_j - 1, 0, len_i - 1

    while top <= bottom and left <= right:
        # 上面一行
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # 右邊一行
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            # 下面一行
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            # 左邊一行
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

print(spiralOrder([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20],
    [21,22,23,24]
]))