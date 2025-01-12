class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        dp = {}

        def dfs(i, j, neu):
            if (i, j, neu) in dp:
                return dp[(i, j, neu)]
            
            if i >= len(coins) or j >= len(coins[0]): 
                return float('-inf')

            if i == len(coins) - 1 and j == len(coins[0]) - 1:
                if coins[i][j] >= 0 or neu > 0:
                    return max(0, coins[i][j])  
                return coins[i][j] 
            max_res = float('-inf')

            if coins[i][j] >= 0:
                max_res = max(max_res, coins[i][j] + dfs(i + 1, j, neu))
                max_res = max(max_res, coins[i][j] + dfs(i, j + 1, neu))
            else:
                if neu > 0:
                    max_res = max(max_res, dfs(i + 1, j, neu - 1))
                    max_res = max(max_res, dfs(i, j + 1, neu - 1))
                max_res = max(max_res, coins[i][j] + dfs(i + 1, j, neu))
                max_res = max(max_res, coins[i][j] + dfs(i, j + 1, neu))

            dp[(i, j, neu)] = max_res
            return max_res

        return dfs(0, 0, 2)
