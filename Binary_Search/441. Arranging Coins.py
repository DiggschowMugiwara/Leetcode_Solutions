
class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        l,r = 0,n
        while l <= r:
            mid = (l+r)//2
            sum_till = (mid)*(mid+1)//2
            if sum_till > n:
                r = mid - 1
            else:
                l = mid + 1
        return r

//TIME COMPLEXITY:O(LOGN)
//SPACE COMPLEXITY:O(1)
