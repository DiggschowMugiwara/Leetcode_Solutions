class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        def func(day):
            if day == len(days):
                return 0
            if day in dp:
                return dp[day] 
            dp[day] = float('inf')
            for d,c in zip([1,7,30],costs):
                j = day
                while j < len(days) and days[j] < days[day] + d:
                    j += 1
                dp[day] = min(dp[day],c + func(j))
            return dp[day]

        return func(0)
        
