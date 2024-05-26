def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for string in s:
        if(string == '(' or string == '{' or string == '['):
            stack.append(string)
        elif(string == ')' and stack and stack[-1] == '('):
            del stack[-1]
        elif(string == '}' and stack and stack[-1] == '{'):
            del stack[-1]
        elif(string == ']' and stack and stack[-1] == '['):
            del stack[-1]
        else:
            return False
    return stack == []

def otherIsValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for string in s:
        if string in mapping.values():
            stack.append(string)
        elif stack and stack[-1] == mapping[string]:
            del stack[-1]
        else:
            return False
    return stack == []


answers = {'()':True, '()[]{}':True, '(]':False, '[':False, ']':False}

for key, value in answers.items():
    output = otherIsValid(key)
    if output != value:
        print(f'Key: {key}, Value: {value}, Output: {output}')