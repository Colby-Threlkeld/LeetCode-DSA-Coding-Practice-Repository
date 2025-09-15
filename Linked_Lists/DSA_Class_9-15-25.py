# using deque as a stack in class

from collections import deque

#right-end stack
st = deque()
st.append(1)
st.pop()

#left-end stack
st2 = deque()
st.appendleft(2)
st.popleft()

# using deque as a queue

#left in right out
q = deque()
q.appendleft(1)
q.pop()

#right in left out
q2 = deque()
q2.append(1)
q2.popleft()

# LINKED LIST implementation:

class Node:
    def __init__ (self, val= None, next= None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    # inserting a new item at the TAIL of LL --> Time Complexity O(1)
    def addLast(self, val):
        new_node = node(val)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # inserting a node at the HEAD of a LL --> Time Complexity O(1)
    def addFirst(self, val):
        new_node = Node(val)

        if self.is_empty():
            self.head = self.tail = new_node
        else: 
            new_node.next = self.next
            self.head = new_node

    # finding an item at index --> O(n), by value --> O(n) (Time Complexity)
    def indexOf(self, val):
        idx = 0
        curr = self.head

        while curr is not None:
            if curr.val == val:
                return idx
            curr = curr.next
            idx += 1
        return -1
    
    def contains(self, val):
        return self.indexOf(val) != -1
