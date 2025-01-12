class Solution:
    def checkValidString(self, s: str) -> bool:
        locked = []
        unlocked = []
        for i in range(len(s)):
            if s[i] == '(':
                locked.append(i)
            elif s[i] == '*':
                unlocked.append(i)
            else:
                if len(locked) > 0:
                    locked.pop()
                elif len(unlocked) > 0:
                    unlocked.pop()
                else:
                    return False
        while locked and unlocked and locked[-1] < unlocked[-1]:
            locked.pop()
            unlocked.pop()
        if len(locked) > 0:
            return False
        return True


# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(N)
