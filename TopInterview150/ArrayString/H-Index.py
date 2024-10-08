class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)
        h = 0

        for citation in citations:
            if citation > h:
                h += 1
            else:
                break

        return h
    
s = Solution()
print(s.hIndex([3, 0, 6, 1, 5]))