'''
Learning to create Two Stacks from a single list: 9/9/25

Concepts:
A stack is a data structure that follows the Last In First Out (LIFO) principle
stack overflow will occur if you try to push an item onto a full stack (if the top pointer = max size - 1, the stack is considered full)
stack underflow will occur if you try to pop an item from an empty stack (if the top pointer = -1, the stack is considered empty)
'''

class TwoStacks:
    def __init__ (self, n):
        self.size = n
        self.elements - [None] * n
        self.top_left_side = -1 # left stack starts from the start of the array
        self.top_right_side = n # right stack starts from the end of the array

    def push_left(self, item):
        if self.top_left_side + 1 == self.top_right_side: # if the next index for the left stack is the same as the right, raise an error
            raise IndexError("Stack Overflow")
        
        self.top_left_side += 1 # increments the left pointer forward 
        self.elements[self.top_left_side] = item # adds the item to the top of the stack

# same logic as push_left but for the right stack
    def push_right(self, item):
        if self.top_right_side - 1 == self.top_left_side: 
            raise IndexError("Stack Overflow")
        
        self.top_right_side -= 1
        self.elements[self.top_right_side] = item

    def pop_left(self):
        if self.top_left_side == -1:
            raise IndexError("Stack Underflow")
        
        item = self.elements[self.top_left_side] # store the current element in item
        self.elements[self.top_left_side] = None # set current element to a null value
        self.top_left_side -= 1 # increment the pointer back one
        return item

# same logic as pop left
    def pop_right(self):
        if self.top_right_side == self.size:
            raise IndexError("Stack Underflow")
        
        item = self.elements[self.top_right_side]
        self.elements[self.top_right_side] = None
        self.top_right_side += 1
        return item

    def len_left(self):
        return self.top_left_side + 1

    def len_right(self):
        return self.size - self.top_right_side

    def transfer_to_left(self, n):
        for i in range(n):
            item = self.pop_right()
            self.push_left(item)

    def transfer_to_right(self, n):
        for i in range(n):
            item = self.pop_left()
            self.push_right(item)