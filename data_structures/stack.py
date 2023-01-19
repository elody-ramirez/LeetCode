# There are four ways in which we can carry out the implementation of a stack in Python-

# list
# collections.deque
# queue.LifoQueue
# Singly-linked list

# Out of these three, the easiest and the most popular way for
# implementing a stack in Python is list. Let’s see the implementation
# of a stack in Python using lists.

# Stack implementation using 
# LIST

from queue import LifoQueue
from collections import deque

stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())

########################################################################

# Stack implementation using
# collections.deque

stack = deque()

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())

########################################################################

# Python program to
# demonstrate stack implementation
# using queue module

# Initializing a stack
stack = LifoQueue(maxsize=3)

# qsize() show the number of elements
# in the stack
print(stack.qsize())

# put() function to push
# element in the stack
stack.put('a')
stack.put('b')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
