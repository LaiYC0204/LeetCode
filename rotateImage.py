# 儲存在另一個list內
def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    result = [[] for n in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            result[j].insert(0, matrix[i][j])

    return result

# GPT教自己寫
def GPTrotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # 三角形互換位置
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 翻轉每一行
    for k in range(n):
        for l in range(n // 2):
            matrix[k][l], matrix[k][n - l - 1] = matrix[k][n - l - 1], matrix[k][l]

    return matrix

print(GPTrotate([
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]]
))
