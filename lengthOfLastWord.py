def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    output = 1
    check = True
    for word in s[::-1]:
        if check:
            if word != " ":
                check = False
        else:
            if word == " ":
                return output
            output += 1
    return output

def otherLengthOfLastWord(s):
    sl = s.strip() #移除字串左右兩邊的空白
    sl = sl.split(" ") #以空白分割字串
    return len(sl[-1])

s = 'Hello World'
otherLengthOfLastWord(s)

answers = {'Hello World':5, '   fly me   to   the moon  ':4, 'a':1}
for key, value in answers.items():
    output = lengthOfLastWord(key)
    if output != value:
        print(f'Key: {key}, Value: {value}, Output: {output}')