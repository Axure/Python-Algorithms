from typing import *
import typing
from systems import type_check
from pyalgo.data_structure.queue import PriorityQueue

# TODO: automatically enlarge the matrix space.
class Graph:
    def __init__(self, matrix: [[float]]=[[]]):
        self.nodes = {}
        self.nodes_name = []
        self.edges = {}
        self.edges_reverse = PriorityQueue(lambda x_, y_: self.edges[x_] < self.edges[y_])
        # for row in len():
        #     for column in row:
        #         if column

    # @type_check
    def add_node(self, name: str):
        if name not in self.nodes:
            size = len(self.nodes)
            self.nodes[name] = size
            self.nodes_name.append(name)

    # @type_check
    def get_node_index(self, name: str):
        return self.nodes[name]

    # @type_check
    def add_edge(self, name_a: str, name_b: str, weight: float):
        self.add_node(name_a)
        self.add_node(name_b)
        node_a = self.get_node_index(name_a)
        node_b = self.get_node_index(name_b)
        self.edges[(node_a, node_b)] = weight
        self.edges_reverse.push((node_a, node_b))

    def get_edge(self, name_a: str, name_b: str) -> float:
        node_a = self.get_node_index(name_a)
        node_b = self.get_node_index(name_b)
        return self.get_edge_from_index(node_a, node_b)

    def get_edge_from_index(self, index_a: int, index_b: int) -> float:
        if (index_a, index_b) in self.edges:
            return self.edges[(index_a, index_b)]
        else:
            return 0

    def get_node_name(self, index: int) -> str:
        return self.nodes_name[index]

    def __repr__(self):
        size = len(self.nodes)
        result = ' , '
        for i in range(0, size):
            result += self.get_node_name(i) + ', '
        result += '\n'
        for i in range(0, size):
            result += self.get_node_name(i) + ', '
            for j in range(0, size):
                weight = 0
                if (i, j) in self.edges:
                    weight = self.edges[(i, j)]
                result += str(weight) + ', '
            result += '\n'
        return result

    def __getitem__(self, item):
        print(item)
        if isinstance(item, tuple):
            result = ''
            result += self.get_node_name(item[0]) + ' to ' + self.get_node_name(item[1]) + ': '
            result += 'weight ' + str(self.get_edge_from_index(item[0], item[1]))
            return result
        else:
            return self.get_node_name(item)


if __name__ == '__main__':
    graph = Graph([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_edge("A", "A", 1)
    graph.add_edge("A", "B", 4)
    graph.add_edge("B", "B", 3)
    graph.add_edge("B", "A", 2)
    print(graph)
    print(graph[1])
    print(graph[1, 0])
    print(graph.edges_reverse)
