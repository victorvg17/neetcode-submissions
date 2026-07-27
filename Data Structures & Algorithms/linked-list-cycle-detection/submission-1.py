# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        visitedNodes = set()
        curr = head.next
        while curr:
            if curr in visitedNodes:
                return True
            visitedNodes.add(curr)
            curr = curr.next
        return False

            
        