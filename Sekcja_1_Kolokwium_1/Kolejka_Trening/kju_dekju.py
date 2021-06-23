from collections import deque

my_queue = deque()

my_queue.append("a")
print(my_queue)
my_queue.append("b")
print(my_queue)
my_queue.appendleft("c")
print(my_queue)
my_queue.rotate(2)
print(my_queue)
my_queue.popleft()
print(my_queue)
my_queue.pop()
print(my_queue)