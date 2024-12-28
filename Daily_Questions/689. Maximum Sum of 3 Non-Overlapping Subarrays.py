class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sub_sums = [sum(nums[:k])]
        for i in range(k,len(nums)):
            sub_sums.append(sub_sums[-1]-nums[i-k]+nums[i])
        dp = {}
        def dfs(i,n):
            if (i,n) in dp:
                return dp[(i,n)]
            if n == 3 or i > len(nums)-k:
                return 0


            pick =sub_sums[i] + dfs(i+k,n+1)
            no_pick = dfs(i+1,n)
            dp[(i,n)] = max(pick,no_pick)
            return max(pick,no_pick)
        i = 0
        ind = []
        print(dfs(0,0))
        while i <= len(nums)-k and len(ind) < 3:
            include = sub_sums[i] + dfs(i+k,len(ind)+1)
            skip = dfs(i+1,len(ind))
            if include >= skip:
                ind.append(i)
                i += k
            else: i+=1
        return ind
