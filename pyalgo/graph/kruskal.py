from pyalgo.graph.graph import Graph
# from systems.extend import extend
from systems.type_check import type_checked


# @extend(Graph)
# class Graph:
#     def kruskal(self, source, dest):
#         return 0


# @type_checked
def kruskal(g: Graph) -> (float, list):
    count = 0
    weight_sum = 0
    tree = []
    while count < g.size() - 1:
        top_edge = g.get_top_edge()
        weight_sum += g.get_edge_from_pair(top_edge)
        tree.append(top_edge)
        g.pop_edge()
        count += 1
    return float(weight_sum), tree


if __name__ == '__main__':
    A = Graph()
    A.add_node("0")
    A.add_node("1")
    A.add_node("2")
    A.add_edge("0", "0", 1)
    A.add_edge("0", "1", 2)
    A.add_edge("0", "2", 3)
    A.add_edge("1", "0", 4)
    A.add_edge("1", "1", 5)
    A.add_edge("1", "2", 6)
    A.add_edge("2", "0", 7)
    A.add_edge("2", "1", 8)
    A.add_edge("2", "2", 9)
    print(A.size())
    print(kruskal(A))
    print(3)

    B = Graph()
    B.add_node("A")
    B.add_node("B")
    B.add_node("C")
    B.add_node("D")
    B.add_node("E")
    B.add_node("F")
    B.add_node("G")
    B.add_node("H")
    B.add_node("I")
    B.add_edge("A", "B", 3)
    B.add_edge("A", "F", 2)
    B.add_edge("B", "C", 17)
    B.add_edge("B", "D", 16)
    B.add_edge("C", "I", 18)
    B.add_edge("D", "E", 11)
    B.add_edge("D", "I", 4)
    B.add_edge("E", "H", 5)
    B.add_edge("E", "I", 10)
    B.add_edge("F", "E", 1)
    B.add_edge("F", "G", 7)
    B.add_edge("G", "H", 15)
    B.add_edge("H", "J", 13)
    print(kruskal(B))
