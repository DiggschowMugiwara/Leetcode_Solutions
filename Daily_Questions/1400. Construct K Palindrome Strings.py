class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        hsh = Counter(s)
        print(hsh)
        maxp = 0
        no_of_odd = 0
        odd_val = None
        for key in hsh:
            if hsh[key]%2 == 1:
                no_of_odd += 1
            else:
                while hsh[key] > 0:
                    hsh[key] -= 2
                    maxp += 1
        print(maxp)
        if no_of_odd > k:
            return False
        return True



# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(N)
