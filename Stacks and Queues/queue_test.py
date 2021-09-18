from queues import QueueNode, Queue

obj = Queue()
obj.add(QueueNode(1))
obj.add(QueueNode(2))
obj.peek()
obj.pop()
obj.empty()