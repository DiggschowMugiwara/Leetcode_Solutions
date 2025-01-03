class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        prefix_sums = []
        for i in range(len(nums)):
            if i == 0:
                prefix_sums.append(nums[i])

            else:
                prefix_sums.append(prefix_sums[i-1] + nums[i])
        tsum = sum(nums)
        res = 0
        for i in range(len(nums)-1):
            if prefix_sums[i] >= tsum - prefix_sums[i]:
                res += 1
        # print(prefix_sums)
        return res

# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(N)
