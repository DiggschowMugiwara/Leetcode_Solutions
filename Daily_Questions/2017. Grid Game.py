class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        frst = [grid[0][0]]
        scnd = [grid[1][-1]]
        for i in range(1,len(grid[0])):
            frst.append(frst[-1] + grid[0][i])
        for i in range(len(grid[0])-2,-1,-1):
            scnd.append(scnd[-1] + grid[1][i])
        scnd = scnd[::-1]

        mini = float('inf')
        for i in range(len(frst)):
            temp = max(frst[-1] - frst[i],scnd[0] - scnd[i])
            mini = min(mini,temp)
        return mini


# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(N)
