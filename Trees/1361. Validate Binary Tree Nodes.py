class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        par = set(leftChild + rightChild)
        par.discard(-1)
        for i in range(n):
            if i not in par:
                break
        root = i
        visited = set()
        # visited.add(root)
        q = [root]
        while q:
            x = q.pop(0)
            print(x)
            if x in visited:
                return False
            visited.add(x)
            if leftChild[x] != -1:
                q.append(leftChild[x])
            if rightChild[x] != -1:
                q.append(rightChild[x])
        print("hii")
        return (len(visited) == n)
            
#TIME COMPLEXITY : O(N)
#SPACE COMPLEXITY : O(N)
