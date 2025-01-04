class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = [0] * 52
        odd_count = 0

        for char in s:
            idx = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a') + 26
            count[idx] ^= 1
            odd_count += 1 if count[idx] else -1

        return len(s) - max(odd_count - 1, 0)

        