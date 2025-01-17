class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        if k == 0:
            return sum(reward2)
        min_heap = []
        for i in range(len(reward1)):
            if len(min_heap) < k:
                heapq.heappush(min_heap,reward1[i]-reward2[i])
            else:
                if min_heap[0] < reward1[i]-reward2[i]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap,reward1[i]-reward2[i])

        print(min_heap)
        res = sum(reward2)
        res += sum(min_heap)
        return res

# TIME COMPLEXITY : O(NLOGK)
# SPACE COMPLEXITY : O(K)
