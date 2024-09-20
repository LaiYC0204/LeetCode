class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        sSplit = s.split()
        for l in sSplit[:0:-1]:
            result += l + ' '

        return result + sSplit[0]
    
    def otherReverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=s.split()
        l.reverse()
        return " ".join(l)
    
s = Solution()
print(s.reverseWords("  hello world  abc"))