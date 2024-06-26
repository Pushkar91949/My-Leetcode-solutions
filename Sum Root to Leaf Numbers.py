# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, curSum):
            if not node:
                return 0
            curSum = curSum * 10 + node.val
            if not node.left and not node.right:
                return curSum
            left_sum = dfs(node.left, curSum)
            right_sum = dfs(node.right, curSum)
            return left_sum + right_sum
        
        return dfs(root, 0)
      # Question link: https://leetcode.com/problems/sum-root-to-leaf-numbers/
