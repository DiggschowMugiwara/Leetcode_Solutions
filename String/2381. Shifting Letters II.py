class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_shift = [0]*(len(s)+1)
        for i in range(len(shifts)):
            if shifts[i][2] == 1:
                prefix_shift[shifts[i][1]+1] += 1
                prefix_shift[shifts[i][0]] -= 1
            else:
                prefix_shift[shifts[i][1]+1] -= 1
                prefix_shift[shifts[i][0]] += 1
        print(prefix_shift)
        for i in range(len(prefix_shift)-2,-1,-1):
            prefix_shift[i] += prefix_shift[i+1]
        res = [ord(c)-ord("a")+26 for c in s]
        for i in range(len(res)):
            res[i] += prefix_shift[i+1]
            res[i] = res[i]%26
        s = [chr(ord('a')+n) for n in res]
        print(s)



        return "".join(s)


# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(N)
