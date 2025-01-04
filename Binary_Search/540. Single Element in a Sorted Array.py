class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        l,r = 0,len(nums)-1
        n = len(nums)
        while l < r:
            mid = (l+r)//2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                l = mid + 2
            else:
                r = mid
        return nums[l]

# TIME COMPLEXITY : O(LOGN)
# SPACE COMPLEXITY : O(1)
