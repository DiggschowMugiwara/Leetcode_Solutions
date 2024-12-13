
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m = len(board)
        n = len(board[0])
        mod = 10**9+7

        dp = [(0,0)]*n 
    
        for i in range(m-1, -1, -1):
            prev = None
            for j in range(n-1, -1, -1):
                cur = dp[j]
                if board[i][j]=='S':
                    dp[j]=(0, 1)
                elif board[i][j]=='X':
                    dp[j] = (float("-inf"),0)
                else:
                    maxval = float("-inf")
                    count = 0
                    if i+1<m:
                        maxval = dp[j][0]
                        count+= dp[j][1]%mod
                    if j+1<n and maxval<=dp[j+1][0]:
                        if maxval < dp[j+1][0]:
                            count = 0
                        count+=dp[j+1][1]%mod
                        maxval = max(maxval, dp[j+1][0])
                    if i+1<m and j+1<n and maxval<=prev[0]:
                        if maxval < prev[0]:
                            count = 0
                        count+=prev[1]%mod
                        maxval = max(maxval, prev[0])
                
                    if maxval==float("-inf"):
                        dp[j] = (float("-inf"),0)
                        prev = cur
                        continue
                    
                    if board[i][j]!='E':
                        maxval+= int(board[i][j])%mod
                    dp[j] = (maxval%mod, count%mod)
                prev = cur
        
        return list(dp[0]) if dp[0][0]!=float("-inf") else [0,0]
