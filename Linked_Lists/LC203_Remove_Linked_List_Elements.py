'''
https://leetcode.com/problems/remove-linked-list-elements/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        temp = ListNode(0) #temporary or "Dummy" node
        temp.next = head #will always store new head

        prev, node = temp, head
        while node:
            #if node = target, previous node points past current node
            if node.val == val:
                prev.next = node.next
            #otherwise, previous node is new current 
            else:
                prev = node
            node = node.next #increment to next node 
        return temp.next #return new head
