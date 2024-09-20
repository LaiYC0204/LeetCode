class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = len(s) - 1
        isSpace = True
        length = 0

        while i >= 0:
            if isSpace:
                if s[i] == " ":
                    i -= 1
                else:
                    isSpace = False
            else:
                if s[i] != " ":
                    length += 1
                    i -= 1
                else:
                    break

        return length
    
    def otherlengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split()
        return len(l[-1])
    
s = Solution()
print(s.otherlengthOfLastWord("Hello World"))