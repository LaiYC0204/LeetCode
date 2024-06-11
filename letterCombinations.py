def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []

    output = []
    generate('', digits, output)
    return output

def generate(current, digits, output):
    combinations = {
        '2':['a','b','c'],
        '3':['d','e','f'], 
        '4':['g','h','i'], 
        '5':['j','k','l'], 
        '6':['m','n','o'], 
        '7':['p','q','r','s'], 
        '8':['t','u','v'], 
        '9':['w','x','y','z']
    }
    if not digits:
        output.append(current)
        return
    else:
        for letter in combinations[digits[0]]:
            generate(current + letter, digits[1:], output)

answers = {"23":["ad","ae","af","bd","be","bf","cd","ce","cf"], "":[], '2':["a","b","c"]}

for key, value in answers.items():
    output = letterCombinations(key)
    if output != value:
        print(f'Key: {key}, Value: {value}, Output: {output}')