# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    first_node = None
    last_node = None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        if not self.first_node:
            self.first_node = head

        if head.next is None:
            self.last_node = head
            return head

        node = self.reverseList(head.next)

        if node is None:
            return None 

        node.next = head
        head.next = None

        if self.first_node == head:
            return self.last_node


        return head

        