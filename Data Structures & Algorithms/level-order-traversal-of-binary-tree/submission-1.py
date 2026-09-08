# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        out = []
        q = collections.deque()
        q.append(root)
        while q:
            arr = []
            for i in range(len(q)):
                last = q.popleft()
                arr.append(last.val)
                if last.left:
                    q.append(last.left)
                if last.right:
                    q.append(last.right)
            out.append(arr)
        return out
        