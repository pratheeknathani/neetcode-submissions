# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = 0
        stack = [[root, root.val]]
        while stack:
            node, val = stack.pop()
            if node:
                if node.val >= val:
                    result += 1
                stack.append((node.left, max(val, node.val)))
                stack.append((node.right, max(val, node.val)))
        return result