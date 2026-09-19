# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, node):
        if node is None:
            return
        self.values.append(node.val)
        self.traverse(node.left)
        self.traverse(node.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.values = []
        self.traverse(root)
        print(f"values={self.values}")
        self.values.sort()
        return self.values[k-1]
        