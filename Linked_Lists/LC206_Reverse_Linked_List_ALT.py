#Link: https://leetcode.com/problems/reverse-linked-list/?envType=problem-list-v2&envId=plakya4j
#Problem 206: Reverse Linked List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

def reversedList(head):
    curr = head
    prev = None

    while curr:
        nextNode = curr.next #Storing the next node (1st iteration is node2)
        curr.next = prev #Points the current node to prev node (1st iteration 1 -> None)
        prev = curr #moves previous node forward (1st iteration None to node1
        curr = nextNode
    return prev

new_head = reversedList(node1)

# print values
curr = new_head

while curr:
    print(curr.val, end="->")
    curr = curr.next
