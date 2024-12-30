class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        cycle_len = 2 * numRows - 2  
        for i, char in enumerate(s):
            row = i % cycle_len
            row = row if row < numRows else cycle_len - row
            rows[row] += char
        return ''.join(rows)

        