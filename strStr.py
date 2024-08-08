def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    for i in range(len(haystack)):
        if haystack[i:len(needle)+i] == needle:
            return i
        
    return -1
    

inputs = [["sadbutsad","sad"], ["leetcode", "leeto"], ['aaa','a'], ['abc', 'c'], ['a','a'], ["mississippi","issip"]]
answers = [0,-1,0,2,0,4]

for i in range(len(inputs)):
    answer = strStr(inputs[i][0], inputs[i][1])
    if answer != answers[i]:
        print(f'input0:{inputs[i][0]} input1:{inputs[i][1]} output:{answer}')
