# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nodeSum = [0]
        helper(root,nodeSum)
        return root
        def helper(root,nodeSum):
            if root == None:
                return
            helper(root.right,nodeSum)
            nodeSum[0] += root.val

            root.val = nodeSum[0]
            helper(root.left,nodeSum)
        # Question link: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
