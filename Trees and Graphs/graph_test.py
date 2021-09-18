from graphs import GraphNode, Graph
from queues import QueueNode, Queue

zero = GraphNode(id=0)
one = GraphNode(id=1)
two = GraphNode(id=2)
three = GraphNode(id=3)
four = GraphNode(id=4)
five = GraphNode(id=5)

zero.add_children([one,four,five])
one.add_children([three,four])
two.add_child(one)
three.add_children([two, four])

obj = Graph()
obj.insert_nodes(0,[one,four,five])
obj.insert_nodes(1,[three,four])
obj.insert_nodes(2,[one])
obj.insert_nodes(3,[two,four])

def bfs(root: GraphNode):
    queue = Queue()
    root.visited = True
    queue.add(QueueNode(data=root))

    while not queue.empty():
        node: GraphNode = queue.pop().data
        node.visited = True
        print(node.id)
        for child in node.children:
            if not child.visited:
                child.visited = True
                queue.add(QueueNode(data=child))

def dfs(root: GraphNode):
    if not root:
        return
    print(root.id)
    root.visited = True
    for node in root.children:
        if not node.visited:
            dfs(node)
bfs(zero)