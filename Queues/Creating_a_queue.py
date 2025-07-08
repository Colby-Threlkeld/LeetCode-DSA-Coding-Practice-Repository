from collections import deque

# Create an empty queue
queue = deque()

# Enqueue (add to the end)
queue.append("A")
print("Enqueued A:", list(queue))

queue.append("B")
print("Enqueued B:", list(queue))

queue.append("C")
print("Enqueued C:", list(queue))

queue.append("D")
print("Enqueued D:", list(queue))

# Dequeue (remove from the front)
first_item = queue.popleft()
print("Dequeued:", first_item)
print("Queue after dequeue:", list(queue))

# Check if queue is empty
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty:", list(queue))

'''
Output: 

Enqueued A: ['A']
Enqueued B: ['A', 'B']
Enqueued C: ['A', 'B', 'C']
Enqueued D: ['A', 'B', 'C', 'D']
Dequeued: A
Queue after dequeue: ['B', 'C', 'D']
Queue is not empty: ['B', 'C', 'D'] 
'''
