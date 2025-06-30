# Link: https://leetcode.com/problems/reverse-linked-list/description/?envType=problem-list-v2&envId=plakya4j
# Problem: LeetCode 206: Reverse Linked List (Best Time: 17:46)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
    
        while curr:
            next_node = curr.next #stores next node before breaking link
            curr.next = prev #reverse pointer to the prev node
            prev = curr #advancing prev forward 
            curr = next_node #advancing curr forward

        return prev # New head of reversed list

