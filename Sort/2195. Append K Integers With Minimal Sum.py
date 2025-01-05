class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
        nums = sorted(set(nums))
        fsum = 0
        missing_sum = 0
        last = 0

        for num in nums:
            spaces = num - last - 1
            if k <= 0:
                break

            if spaces > 0:
                take = min(spaces, k)
                first_missing = last + 1
                last_missing = last + take
                missing_sum += (last_missing * (last_missing + 1)) // 2 - (first_missing * (first_missing - 1)) // 2
                k -= take  
            
            fsum += num
            last = num  

        if k > 0:
            first_missing = last + 1
            last_missing = last + k
            missing_sum += (last_missing * (last_missing + 1)) // 2 - (first_missing * (first_missing - 1)) // 2
        
        return missing_sum

# TIME COMPLEXITY : O(NLOGN)
# SPACE COMPLEXITY : O(1)
            
