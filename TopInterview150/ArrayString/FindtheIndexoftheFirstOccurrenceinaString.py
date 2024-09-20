class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        
    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            for i in range(len(haystack)):
                if needle == haystack[i:i + len(needle)]:
                    return i
        else:
            return -1
    
s = Solution()
print(s.strStr2("123leetcode", "leet"))