from typing import *
import typing
from typings import type_check

# TODO: automatically enlarge the matrix space.
class Graph:
    def __init__(self, matrix: [[float]]=[[]]):
        self.nodes = {}
        self.edges = [[0 for x in range(10)] for x in range(10)]
        for row in matrix:
            for column in row:
                print(column)

    # @type_check
    def add_node(self, name: str):
        if name not in self.nodes:
            size = len(self.nodes)
            self.nodes[name] = size

    # @type_check
    def get_node_order(self, name: str):
        return self.nodes[name]

    # @type_check
    def add_edge(self, name_a: str, name_b: str, weight: float):
        self.add_node(name_a)
        self.add_node(name_b)
        self.edges[self.get_node_order(name_a)][self.get_node_order(name_b)] = weight


if __name__ == '__main__':
    graph = Graph([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("A", "B", 1)
