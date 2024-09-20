class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        result = ''
        strsMinLen = len(min(strs, key=len))

        while i < strsMinLen:
            result += strs[0][i]
            for string in strs[1:]:
                if result != string[0:i+1]:
                    result = string[0:i]
                    return result
            i += 1

        return result
    
    def otherLongestCommonPrefix(self, strs):
        # strs: 冒號結束if語句
        if not strs: return ""
        prefix = strs[0]
        for s in strs[1:]:
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix: return ""
        return prefix
        

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))