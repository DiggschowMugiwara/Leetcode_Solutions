class Solution:
    def smallestString(self, s: str) -> str:
        
        l,r = 0,0
        for c in s:
            if c == 'a' and l == r:
                l += 1
                r += 1
            elif c == 'a':
                break
            else:
                r += 1
        print(f"{l} and {r}")
        new = []
        for i in range(len(s)):
            if i >= l and i < r:
                new.append(chr(ord(s[i])-1))
            else:
                new.append(s[i])
        if l == r and l == len(s):
            s = s[:-1] + "z"
            return s
        return "".join(new)


                
