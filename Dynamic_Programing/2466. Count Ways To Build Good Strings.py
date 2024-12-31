class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = {}
        def dfs(s):
            if s in dp:
                return dp[s]
            if s > high:
                return 0
            res = 0
            if s >= low:
                res = 1
            res += dfs(s + zero) + dfs(s + one)
            dp[s] = res
            return dp[s] % MOD
        return dfs(0)%MOD
            
