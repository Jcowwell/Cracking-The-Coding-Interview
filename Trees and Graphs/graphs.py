from typing import List

class GraphNode:
    def __init__(self, id: int, children: List = None) -> None:
        self.id = id
        self.children = [] if not children else children
        self.visited = False

    def add_child(self, child) -> None:
        self.children.append(child)

    def add_children(self, children) -> None:
        self.children.extend(children)
        
class Graph:
    def __init__(self) -> None:
        self.nodes: List[GraphNode] = []

    def insert_nodes(self, adjacency_index: int, nodes: List[GraphNode]) -> None:
        self.nodes.insert(adjacency_index,nodes)

