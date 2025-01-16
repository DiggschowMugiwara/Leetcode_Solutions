class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        

        xor_od_num2 = 0
        for i in range(len(nums2)):
            xor_od_num2 ^= nums2[i]
        xor_od_num1 = 0
        for i in range(len(nums1)):
            xor_od_num1 ^= nums1[i]
        print(xor_od_num1)
        print(xor_od_num2)
        if len(nums2) % 2 == 0 and len(nums1) % 2 == 0:
            return 0
        if len(nums2) % 2 == 0 and len(nums1) % 2 == 1:
            return xor_od_num2
        if len(nums2) % 2 == 1 and len(nums1) % 2 == 1:
            return xor_od_num2 ^ xor_od_num1
        return xor_od_num1

# TIME COMPLEXITY : O(N)
# SPACE COMPLEXIY : O(1)
