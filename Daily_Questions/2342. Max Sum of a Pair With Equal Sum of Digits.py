class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def find_digsum(num):
            temp = 0
            while num > 0:
                temp += num%10
                num //= 10
            return temp
        hsh = defaultdict(list)
        for i in range(len(nums)):
            x = find_digsum(nums[i])
            hsh[x].append(nums[i])
        print(hsh)
        maxi = -1
        for key in hsh:
            if len(hsh[key]) > 1:
                hsh[key].sort(reverse=True)
                maxi = max(maxi , hsh[key][0] + hsh[key][1])
        return maxi
            
