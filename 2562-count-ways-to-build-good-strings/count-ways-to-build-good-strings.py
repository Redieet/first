class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # DP array to store the number of ways to construct strings of length i
        dp = [0] * (high + 1)
        dp[0] = 1  # Base case: One way to construct a string of length 0 (empty string)
        
        # Fill the DP array
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD
        
        # Sum up the counts for lengths in the range [low, high]
        result = 0
        for i in range(low, high + 1):
            result = (result + dp[i]) % MOD
        
        return result
