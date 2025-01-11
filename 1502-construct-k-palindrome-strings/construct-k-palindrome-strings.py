class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        from collections import Counter
        if k > len(s):
            return False
        odd_count = sum(v % 2 for v in Counter(s).values())
        return odd_count <= k
