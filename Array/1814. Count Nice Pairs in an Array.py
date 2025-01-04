class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        res = 0
        MOD = 10**9 + 7
        def rev(n):
            n = str(n)
            n = n[::-1]
            return int(n)
        diff = defaultdict(int)
        for num in nums:
            x = num - rev(num)
            res += diff[x]
            diff[x] += 1
        return res % MOD

# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(1)
