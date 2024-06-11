def myLengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    max_len = 0
    for i in range(len(s)):
        compar = [s[i]]
        length = 1
        for j in range(i + 1,len(s)):
            if s[j] in compar:
                break
            compar.append(s[j])
            length += 1
        max_len = max(max_len, length)

    return max_len

"""Sliding Window
如果s[right]在集合內的話
檢查s[left]是否為s[right]如果不是left += 1
直到將s[right]從集合內刪除

如果s[right]沒在集合內的話
將s[right]加入集合內
更新max_len
"""
def GPTLengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    max_len = 0
    left = 0
    char_set = set()
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

answers = {'abcabcbb':3, 'bbbbb':1, 'pwwkew':3, ' ':1, '':0, 'aau':2, 'abc':3, 'cdd':2, 'abba':2}

for key, value in answers.items():
    output = GPTLengthOfLongestSubstring(key)
    if output != value:
        print(f'Key: {key}, Value: {value}, Output: {output}')