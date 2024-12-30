class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Constants for 32-bit integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Initialize index, sign, and result
        i, n, result, sign = 0, len(s), 0, 1

        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Check for sign
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Parse digits and build the number
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            
            # Check overflow condition
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1

        return result * sign
