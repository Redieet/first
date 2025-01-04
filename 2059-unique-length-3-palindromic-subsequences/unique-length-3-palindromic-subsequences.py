class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        result = set()
        right = [0] * 26

        for char in s:
            right[ord(char) - ord('a')] += 1

        seen = set()

        for i in range(n):
            mid = s[i]
            right[ord(mid) - ord('a')] -= 1
            for char in seen:
                if right[ord(char) - ord('a')] > 0:
                    result.add(char + mid + char)
            seen.add(mid)

        return len(result)
