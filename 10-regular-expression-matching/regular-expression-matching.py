class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Cache the results of subproblems
        memo = {}

        def dp(i, j):
            """
            Returns True if s[i:] matches p[j:].
            """
            if (i, j) in memo:
                return memo[(i, j)]

            # If we reach the end of the pattern
            if j == len(p):
                result = i == len(s)  # True if both strings are fully matched
            else:
                # First character matches if:
                # - Characters match exactly, or
                # - Pattern has '.' which matches any character
                first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

                # Handle '*' in the pattern
                if j + 1 < len(p) and p[j + 1] == '*':
                    # Two cases:
                    # 1. '*' means zero occurrences of the preceding element (skip "x*").
                    # 2. '*' means one or more occurrences of the preceding element (consume one char).
                    result = dp(i, j + 2) or (first_match and dp(i + 1, j))
                else:
                    # Proceed if first characters match
                    result = first_match and dp(i + 1, j + 1)

            # Cache the result and return it
            memo[(i, j)] = result
            return result

        return dp(0, 0)

        