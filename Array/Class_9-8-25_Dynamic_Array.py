'''
Building a dynamic array from scratch in Python.
'''

def __init__(self):
    self.n = 0
    self.cap = 1
    self.arr = self.make_array(self.cap)

#Used to: len(arr)
def __len__(self):
    return self.n

#Used to: print(arr[i])
def __getitem__(self, k):
    if not 0 <= k < self.n:
        raise IndexError('Invalid Index')
    return self.arr[k]

#Used to: arr.append(val)
def append(self, val):
    if self.n == self.cap:
        self._resize(2 * self.cap)
    self.arr[self.n] = val
    self.n += 1

#Used to: resize the capacity of the array
def _resize(self, new_cap):
    new_arr = self.make_array(new_cap)
    for i in range(self.n):
        new_arr[i] = self.arr[i]
    self.arr = new_arr
    self.cap = new_cap

#Function to create a new array with given capacity
def make_array(self, new_cap):
    return (new_cap * ctypes.py_object)()
