class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # ct = 0
        # res = []
        # for i in range(n+1):
        #     ct = 0
        #     k = i
        #     print(k)
        #     for _ in range(32):
        #         if k & 1:
        #             ct += 1
        #         k = k >> 1
        #     res.append(ct)
        # return res

        offset = 0
        res = []
        off = [2]
        while off[-1] < n:
            off.append(off[-1]*2)
        off = set(off)

        for i in range(n+1):
            if i == 0:
                res.append(0)
            elif i == 1:
                res.append(1)
            else:
                if i in off:
                    offset = i
                res.append(res[i-offset] + 1)
        return res
# TIME COMPLEXITY : O(N)
# SPACE COMPLEXTY : O(N)
