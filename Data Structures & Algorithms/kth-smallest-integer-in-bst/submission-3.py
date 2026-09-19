# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse_in_order(self, node):
        if node is None:
            return
        self.traverse_in_order(node.left)
        self.values.append(node.val)
        self.traverse_in_order(node.right)
    def traverse_pre_order(self, node):
        if node is None:
            return
        self.values.append(node.val)
        self.traverse_pre_order(node.left)
        self.traverse_pre_order(node.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.values = []
        self.traverse_in_order(root)
        print(f"values={self.values}")
        # self.values.sort()
        return self.values[k-1]
        