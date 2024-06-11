def myLongestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    compar = {s[0]:[0]}
    output = ''
    for i in range(len(s)):
        if s[i] in compar:
            for compar_value in compar[s[i]]:
                if i - compar_value + 1 > len(output):
                    palindromic = s[compar_value:i+1]
                    if palindromic == palindromic[::-1]:
                        output = palindromic
            compar[s[i]].append(i)
        else:
            compar[s[i]] = [i]
    if not output:
        output = s[-1]
    return 

#中心扩展法（Expand Around Center）
def otherLongestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if s == s[::-1]:
        return s

    start, size = 1, 0
    print(s)
    for i in range(1, len(s)): #1~10
        left, right = i - size, i + 1
        s1, s2 = s[left-1:right], s[left:right] #, aac
        print(f'left:{left:<2} right:{right:<2} s1:{s1.ljust(10)} s2:{s2.ljust(10)} start:{start:<2} size:{size:<2}')
        if left - 1 >= 0 and s1 == s1[::-1]:
            start, size = left-1, size+2
        elif s2 == s2[::-1]:
            start, size = left, size+1
    
    return s[start:start+size]

answers = {'babad':'aba', 'cbbd':'bb', 'a':'a', 'ccc':'ccc', 'aacabdkacaa':'aca', 'xaabacxcabaaxcabaax':'xaabacxcabaax', 'ababa':'ababa', 'aaaabaaa':'aaabaaa'}

for key,value in answers.items():
    output = otherLongestPalindrome(key)
    if value != output:
        print(f'Key: {key}, Value: {value}, Output: {output}')