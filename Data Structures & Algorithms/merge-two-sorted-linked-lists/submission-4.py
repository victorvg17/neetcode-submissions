# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 == None and list2 == None:
        #     return None
        # curr1, curr2 = list1, list2
        # nodes = []
        # while curr1:
        #     nodes.append(curr1)
        #     curr1 = curr1.next

        # while curr2:
        #     nodes.append(curr2)
        #     curr2 = curr2.next

        # nodes.sort(key=lambda node: node.val)
        # head = nodes[0]
        # curr = head
        # for node in nodes[1:]:
        #     curr.next = node
        #     curr = curr.next
        # curr.next = None
        # return head

        node = ListNode()
        curr = node
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            # val1 is smaller, add it to the merged list
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            # val2 is smaller, add it to the merged list
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next

        if curr1 is None:
            curr.next = curr2
        else:
            curr.next = curr1
        # curr.next = None

        return node.next



        