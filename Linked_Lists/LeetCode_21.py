# Link: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Problem 21: Merge Two Sorted Lists


# Singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
# Dummy node acts as a starting point for merged / linked list
        dummy = ListNode(0)
        current = dummy

# Traverses each list while both have a value
# Compares both current nodes, and adds the smaller value to the merged / linked list
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
# Attatches any remaining elements, considering the possibility one list might have more elements than the other
        current.next = list1 if list1 else list2

# Skips dummy node and returns the merged / linked list
        return dummy.next
