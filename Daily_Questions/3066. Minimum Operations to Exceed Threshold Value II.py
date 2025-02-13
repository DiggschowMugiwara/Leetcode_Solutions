class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        top = nums[0]
        ct = 0
        while top < k:
            # print(nums)
            one = heapq.heappop(nums)
            two = heapq.heappop(nums)
            temp = min(one,two) * 2 + max(one,two)
            heapq.heappush(nums,temp)
            top =  nums[0]
            ct += 1
        return ct
