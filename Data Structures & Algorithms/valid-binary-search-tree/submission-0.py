# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkerHelper(self, node, lower, upper):
        if node is None:
            return True
        return node.val > lower and node.val < upper and self.checkerHelper(node.left, lower, node.val) and self.checkerHelper(node.right, node.val, upper)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lowerBound = float("-inf") 
        upperBound = float("inf")
        return self.checkerHelper(root, lowerBound, upperBound)
        