class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        i = 0
        while i < len(chars):
            let = chars[i]
            ct = 0
            while i < len(chars) and let == chars[i]:
                i += 1
                ct += 1
            chars[ans] = let
            ans += 1
            ct = str(ct)
            if int(ct) > 1:
                for s in ct:
                    chars[ans] = s
                    ans += 1
        return ans

# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(1)
