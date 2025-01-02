class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = set()
        vowels.add('a')
        vowels.add('e')
        vowels.add('i')
        vowels.add('o')
        vowels.add('u')
        prefix_sum = [0]*len(words)
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                if i == 0:
                    prefix_sum[0] = 1
                else:
                    prefix_sum[i] = prefix_sum[i-1] + 1
            else:
                prefix_sum[i] = prefix_sum[i-1]
        res = []
        for q in queries:
            strt,end = 0,0
            if q[0] == 0:
                strt = 0
            else:
                strt = prefix_sum[q[0]-1]
            end = prefix_sum[q[1]]
            res.append(end-strt)
        return res
            

                
# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(N)
