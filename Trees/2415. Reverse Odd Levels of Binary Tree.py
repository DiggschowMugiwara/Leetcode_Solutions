# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        stack = [root.val]
        turn = 1
        while q:
            x = len(q)
            print(f"q is {x}\n")
            if turn % 2 == 1:
                
                for i in range(x):
                    curr = q.pop(0)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                    curr.val = stack.pop()

            else:
                for i in range(x):
                    curr = q.pop(0)
                    if curr.left:
                        stack.append(curr.left.val)
                        q.append(curr.left)
                    if curr.right:
                        stack.append(curr.right.val)
                        q.append(curr.right)   
                print(stack)
            turn += 1
        return root



        # q = [root]
        # turn = 1
        # while q:
        #     x = len(q)
        #     if turn % 2 == 0:
        #         vals = [node.val for node in q]
        #         vals = vals[::-1]
        #         for i in range(x):
        #             q[i].val = vals[i]
        #     for i in range(x):
        #         curr = q.pop(0)
        #         if curr.right:
        #             q.append(curr.right)
        #         if curr.left:
        #             q.append(curr.left)
        #     turn += 1
        # return root


