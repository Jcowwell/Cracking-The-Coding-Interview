

from typing import Optional


class QueueNode:
    def __init__(self, data: any = None, next = None) -> None:
        self.data = data
        self.next = next

class Queue:
    def __init__(self) -> None:
        self.top = QueueNode()
        self.last = self.top

    def add(self, element: QueueNode) -> None:
        """
        Push element x to the back of queue.
        """
        if self.empty():
            self.top = element
            self.last = self.top

        if not self.top.data:
            self.top = element
            self.last = self.top

        self.last.next = element
        self.last = element
        
    def pop(self) -> Optional[QueueNode]:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return None
        temp = self.top
        self.top = self.top.next
        if temp == self.last:
            self.last = None
        return temp
        

    def peek(self) -> Optional[QueueNode]:
        """
        Get the front element.
        """
        return self.top
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.top