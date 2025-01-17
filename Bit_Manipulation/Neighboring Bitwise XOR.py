class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        if len(derived) == 1 and derived[0] == 1:
            return False
        if len(derived) == 1:
            return True
        if derived[0] == 1:
            poss1 = [0,1]
            poss2 = [1,0]
        if derived[0] == 0:
            poss1 = [0,0]
            poss2 = [1,1]
        for i in range(1,len(derived)-1):
            if derived[i] == 0:
                poss1.append(poss1[-1])
                poss2.append(poss2[-1])
            else:
                poss1.append(abs(poss1[-1]-1))
                poss2.append(abs(poss2[-1]-1))
        print(poss1)
        print(poss2)
        if poss1[0] ^ poss1[-1] == derived[-1]:
            return True
        if poss2[0] ^ poss2[-1] == derived[-1]:
            return True
        return False


# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(N)
