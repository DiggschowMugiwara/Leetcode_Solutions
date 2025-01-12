class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        nlocked = []
        unlocked = []
        for i in range(len(locked)):
            if locked[i] == '0':
                unlocked.append(i)
            else:
                if s[i] == '(':
                    nlocked.append(i)
                else:
                    if len(nlocked) > 0:
                        nlocked.pop()
                    elif len(unlocked) > 0:
                        unlocked.pop()
                    else:
                        return False
        while nlocked and unlocked and nlocked[-1] < unlocked[-1]:
            nlocked.pop()
            unlocked.pop()
        if nlocked:
            return False
        return len(unlocked)%2 == 0



# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(N)
