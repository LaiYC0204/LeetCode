class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        rows = [''] * numRows
        current_i = 0
        going_down = True
        result = ''

        for string in s:
            if going_down:
                if current_i < numRows:
                    rows[current_i] += string
                    if current_i == numRows - 1:
                        going_down = False
                        current_i -= 1
                    else:
                        current_i += 1
            else:
                if current_i >= 0:
                    rows[current_i] += string
                    if current_i == 0:
                        going_down = True
                        current_i += 1
                    else:
                        current_i -= 1

        for row in rows:
            result += row

        return result
    
    def otherconvert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        rows = [''] * numRows
        current_i = 0
        going_down = False

        for string in s:
            rows[current_i] += string
            if current_i == 0 or current_i == numRows - 1:
                going_down = not going_down

            if going_down:
                current_i += 1
            else:
                current_i -= 1

        return ''.join(rows)

                
s = Solution()
print(s.otherconvert("PAYPALISHIRING", 4))