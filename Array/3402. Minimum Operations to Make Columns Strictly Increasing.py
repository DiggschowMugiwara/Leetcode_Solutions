class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        res = 0
        for i in range(m):
            for j in range(n):
                if j == 0:
                    ref = grid[j][i]
                else:
                    if grid[j][i] > ref:
                        ref = grid[j][i]
                    else:
                        res += (ref - grid[j][i] + 1)
                        ref = ref + 1
        return res


# TIME COMPLEXITY : 0(M,N)
# SPACE COMPLEXITY : O(1)
