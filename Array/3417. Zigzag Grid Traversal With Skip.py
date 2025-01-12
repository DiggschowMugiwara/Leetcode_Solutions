class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(grid)):
            if i % 2 == 0:
                for j in range(len(grid[0])):
                    if i % 2 == j % 2:
                        res.append(grid[i][j])
            else:
                for j in range(len(grid[0])-1,-1,-1):
                    if i % 2 == j % 2:
                        res.append(grid[i][j])

        return res
# TIME COMPLEXITY : O(MN)
# SPACE COMPLEXITY : O(1)
