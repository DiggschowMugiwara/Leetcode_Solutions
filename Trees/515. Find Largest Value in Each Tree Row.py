# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        q = [root]
        while q:
            x = len(q)
            curr_max = float('-inf')
            for i in range(x):
                curr = q.pop(0)
                curr_max = max(curr_max,curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(curr_max)
        return res
            
#TIME COMPLEXITY : O(V)
#SPACE COMPLEXITY : O(V)
