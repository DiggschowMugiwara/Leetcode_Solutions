class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(32):
            ct = 0
            for j in range(len(nums)):
                # print(f"{nums[j]} and {i} and {(nums[j] >> i) & 1}")
                if (nums[j] >> i) & 1:
                    ct += 1
            
            if ct >= k:
                print(f"hi and {i}")
                res = res | (1 << i)
                # print(res)
                # res = res << 1
            print(res)
        return res


# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(1)
