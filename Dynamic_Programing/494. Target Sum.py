class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:




        
        # length = len(nums)
        # dp = {}
        # def rec(tracker,tsum):
        #     if tracker == length:
        #         if tsum == target:
        #             return 1
        #         return 0
        #     if (tracker,tsum) in dp:
        #         return dp[(tracker,tsum)]
        #     dp[(tracker,tsum)] = rec(tracker+1,tsum + nums[tracker])+rec(tracker+1,tsum - nums[tracker])
        #     return dp[(tracker,tsum)]
        # return rec(0,0)
        n = len(nums)
        val = 0
        dp = defaultdict(int)
        def dfs(i,tsum):
            if i == n:
                if tsum == target:
                    return 1
                else:
                    return 0
            if (i,tsum) in dp:
                return dp[(i,tsum)]
            dp[(i,tsum)] = dfs(i+1,tsum+nums[i])+dfs(i+1,tsum-nums[i])
            return dp[(i,tsum)]
        return dfs(0,0)


# TIME COMPLEXITY : O(N.S)
# SPACE COMPLEXITY : O(N.S)

