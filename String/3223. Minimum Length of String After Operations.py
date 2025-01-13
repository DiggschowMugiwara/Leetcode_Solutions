class Solution:
    def minimumLength(self, s: str) -> int:
        hsh = Counter(s)
        res = 0
        print(hsh)
        for key in hsh:
            if hsh[key] % 2 == 1:
                res += (hsh[key]-1)
            else:
                res += (hsh[key]-2)
        return len(s)-res








# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(N)










        # before = defaultdict(list)
        # after = defaultdict(list)
        # for i in range(1,len(s)):
        #     after[s[i]].append(i)
        # for i in range(1,len(s)):
        #     if s[i] == "*":
        #         continue
        #     before[s[i-1]].append(i-1)
        #     after[s[i]].pop(0)
        #     while before[s[i]] != [] and after[s[i]] != []:
        #         x = before[s[i]].pop()
        #         s = s[:x] + "*" + s[x+1:]
        #         y = after[s[i]].pop(0)
        #         s = s[:y] + "*" + s[y+1:]
        # res = 0
        # for i in range(len(s)):
        #     if s[i] == "*":
        #         continue
        #     res += 1
        # return res
            
