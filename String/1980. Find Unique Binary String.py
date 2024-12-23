class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        orig = len(nums[0])
        r = '0'*len(nums[0])
        for i in range(len(nums)):
            nums[i] = int(nums[i],2)
        print(nums)
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if nums[i] == res:
                res += 1
            else:
                break
        re = str(bin(res)[2:])
        print(re)
        r = r[:orig-len(re)] + re

        return r


# TIME COMPLEXITY : O(NLOGN)
# SPACE COMPLEXITY : O(N)
