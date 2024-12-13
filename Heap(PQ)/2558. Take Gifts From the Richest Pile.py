class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = []
        left_over = []
        for i in range(len(gifts)):
            heapq.heappush(max_heap,-gifts[i])
        for i in range(k):
            x = heapq.heappop(max_heap)
            x = -x
            heapq.heappush(max_heap,-int(pow(x,0.5)))
        return -sum(max_heap)


//TIME COMPLEXITY:O(NLOGN)
//SPACE COMPLEXITY:O(N)
