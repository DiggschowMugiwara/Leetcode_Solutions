
class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        min_heap = []
        for i in range(len(nums)):
            heapq.heappush(min_heap,(nums[i],i))
        score = 0
        marked = [0]*len(nums)
        while min_heap:
            x,index = heapq.heappop(min_heap)
            if marked[index] == 1:
                continue
            marked[index] = 1
            score += x
            if index+1 < len(nums):
                marked[index+1] = 1
            if index-1 >= 0:
                marked[index-1] = 1
        return score
        

  //TIME COMPLEXITY:O(NLOGN)
  //SPACE COMPLEXITY:O(N)
