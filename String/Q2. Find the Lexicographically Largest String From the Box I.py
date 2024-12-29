class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        poss_len = len(word) - numFriends + 1
        lexographically_largest = word[:poss_len]
        print(lexographically_largest)
        for i in range(1,len(word)):
            # print("Hoo")
            if i + poss_len < len(word):
                if word[i] >= lexographically_largest[0]:
                    if word[i:i+poss_len] > lexographically_largest:
                        lexographically_largest = word[i:i+poss_len]
            else:
                if word[i] >= lexographically_largest[0]:
                    if word[i:] > lexographically_largest:
                        lexographically_largest = word[i:]
        return lexographically_largest


# TIME COMPLEXITY : O(n.k)
# SPACE COMPLEXITY: O(k)
