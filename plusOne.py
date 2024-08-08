def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits[-1] += 1
    for i in range(len(digits)-1,-1,-1):
        if digits[i] == 10:
            if i != 0:
                digits[i] = 0
                digits[i-1] += 1
            else:
                digits[0] = 0
                digits.insert(0, 1)
        else:
            break
    return digits

inputs = [[1,2,3], [4,3,2,1],[9]]
answers = [[1,2,4], [4,3,2,2], [1,0]]

for length in range(len(inputs)):
    output = plusOne(inputs[length])
    if answers[length] != output:
        print(length)
        print(f'input:{inputs[length]} output:{output} answer:{answers[length]}')
