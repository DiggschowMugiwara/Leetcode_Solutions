class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        p1,p2 = 0,0
        res = [0]*len(nums)
        curr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                res[curr] = nums[i]
                curr += 1
        return res
