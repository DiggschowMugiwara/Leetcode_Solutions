class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def dfs(step):
            if step in dp:
                return dp[step]
            if step > len(cost)-1 :
                return 0
            one = cost[step] + dfs(step + 1)
            two = cost[step] + dfs(step + 2)
            dp[step] = min(one,two)
            return dp[step]
        return min(dfs(0),dfs(1))
