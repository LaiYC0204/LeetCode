def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    output = ''
    while(num > 0):
        if num >= 1000:
            output += 'M'
            num -= 1000
        elif num >= 900:
            output += 'CM'
            num -= 900
        elif num >= 500:
            output += 'D'
            num -= 500
        elif num >= 400:
            output += 'CD'
            num -= 400
        elif num >= 100:
            output += 'C'
            num -= 100
        elif num >= 90:
            output += 'XC'
            num -= 90
        elif num >= 50:
            output += 'L'
            num -= 50
        elif num >= 40:
            output += 'XL'
            num -= 40
        elif num >= 10:
            output += 'X'
            num -= 10
        elif num >= 9:
            output += 'IX'
            num -= 9
        elif num >= 5:
            output += 'V'
            num -= 5
        elif num >= 4:
            output += 'IV'
            num -= 4
        elif num >= 1:
            output += 'I'
            num -= 1

    return output

def otherIntToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    romans = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100],["XC", 90], ["L", 50], ["XL", 40], ["X", 10], ["IX", 9],["V", 5], ["IV", 4], ["I", 1]]
    output = ''
    for roman, index in romans:
        while num >= index:
            num -= index
            output += roman

    return output

answers = {3749:"MMMDCCXLIX", 58:"LVIII", 1994:"MCMXCIV"}

for key, value in answers.items():
    output = otherIntToRoman(key)
    if output != value:
        print(f'Key: {key}, Value: {value}, Output: {output}')