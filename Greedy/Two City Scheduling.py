class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        min_heap = []
        for i in range(len(costs)):
            if len(min_heap) == len(costs)//2:
                if costs[i][0] - costs[i][1] < -min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap,(-(costs[i][0]-costs[i][1]),i))
            else:
               heapq.heappush(min_heap,(-(costs[i][0]-costs[i][1]),i)) 
        a_set = set()
        while min_heap:
            x,y = heapq.heappop(min_heap)
            a_set.add(y)
        res = 0
        for i in range(len(costs)):
            if i in a_set:
                res += costs[i][0]
            else:
                res += costs[i][1]

        return res
# TIME COMPLEXITY : O(NLOGN)
# SPACE COMPLEXITY : O(N)
