class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        n = len(s)
        result = roman[s[n-1]]

        for i in range(n - 2, -1, -1):
            current = roman[s[i]]
            if current >= roman[s[i + 1]]:
                result += current
            else:
                result -= current

        return result
    
s = Solution()
print(s.romanToInt("MCMXCIV"))