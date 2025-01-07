class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j] or (words[j] in words[i]):
                    if len(words[i]) < len(words[j]):
                        res.add(words[i])
                    else:
                        res.add(words[j])
        return list(res)


# TIME COMPLEXITY : O(N^2M)
# SPACE COMPLEXITY : O(N)
