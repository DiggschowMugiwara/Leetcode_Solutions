class Solution:
    def bestClosingTime(self, customers: str) -> int:
        hsh = Counter(customers)
        initialPenalty = hsh['Y']
        res = initialPenalty
        best = 0
        print(initialPenalty)
        for i in range(len(customers)):
            if customers[i] == 'Y':
                initialPenalty -= 1
            else:
                initialPenalty += 1
            if initialPenalty < res:
                print(f"{res} and {initialPenalty} and {i}")
                best = i + 1
                res = initialPenalty
        return best
        

# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(1)
