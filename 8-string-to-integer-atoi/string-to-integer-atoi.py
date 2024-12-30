class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Constants for 32-bit integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Step 1: Skip leading whitespace
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1

        # If the string is empty or only whitespace, return 0
        if i == n:
            return 0

        # Step 2: Determine the sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # Step 3: Parse the number
        result = 0
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')  # Convert char to int
            # Check for overflow/underflow before adding the digit
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1

        return sign * result
