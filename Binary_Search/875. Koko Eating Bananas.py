class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def find_steps(x):
            steps = 0
            for pile in piles:
                steps += math.ceil(pile / x)
            return steps

        l, r = 1, max(piles) 
        while l < r:
            mid = (l + r) // 2
            if find_steps(mid) <= h:
                r = mid
            else:
                l = mid + 1
        return l  
# TIME COMPLEXITY : O(NLOGN)
# SPACE COMPLEXITY : O(N)
