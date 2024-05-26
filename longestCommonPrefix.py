def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    output = ''
    check = True
    i = 0

    while check and i < len(min(strs, key=len)):
        output += strs[0][i]
        for string in strs[1:]:
            if output != string[0:i+1]:
                check = False
                output = output[0:i]
                break
        i += 1
    return output

answers = {"fl":["flower","flow","flight"], "":["dog","racecar","car"], "":["reflower","flow","flight"]}

for key, value in answers.items():
    output = longestCommonPrefix(value)
    if output != key:
        print(f'Key: {value}, Value: {key}, Output: {output}')