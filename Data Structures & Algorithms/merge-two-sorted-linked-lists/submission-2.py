# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        curr1, curr2 = list1, list2
        nodes = []
        while curr1:
            nodes.append(curr1)
            curr1 = curr1.next

        while curr2:
            nodes.append(curr2)
            curr2 = curr2.next

        nodes.sort(key=lambda node: node.val)
        head = nodes[0]
        curr = head
        for node in nodes[1:]:
            curr.next = node
            curr = curr.next
        curr.next = None
        return head


        