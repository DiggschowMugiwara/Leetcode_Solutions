class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hsh = Counter(s)
        visited = set()
        checked = set()
        for i in range(len(s)):
            hsh[s[i]] -= 1
            for vis in visited:
                if hsh[vis] > 0:
                    checked.add((vis,s[i]))
            visited.add(s[i])
        return len(checked)


# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(N)
