import networkx as nx
from networkx_viewer import Viewer
import pygraphviz as pgv


class matrix:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.matrix = [[0 for x in range(dimension)] for x in range(dimension)]

    def toNetworkxGraph(self):
        G = nx.Graph()
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.matrix[i][j] != 0:
                    G.add_edge(i, j)
        return G

    def toGraphvizGraph(self):
        G = pgv.AGraph()
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.matrix[i][j] != 0:
                    G.add_edge(i + 1, j + 1)
        return G


def dfs(a: matrix, entry: int):
    print('DFS!')
    stack = [entry]
    visited = [0 for x in range(a.dimension)]
    visited[entry] = 1
    while len(stack) != 0:
        top = stack.pop()
        print(top + 1)
        for i in range(a.dimension):
            if a.matrix[top][i] != 0 and visited[i] == 0:
                stack.append(i)
                visited[i] = 1


if __name__ == '__main__':
    print(3)
    M = matrix(6)
    M.matrix = [
        [0, 1, 1, 0, 1, 0],
        [1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 1],
        [0, 0, 1, 0, 1, 0],
    ]
    # G = M.toGraph()
    # G = nx.Graph()
    # G.add_edge(1, 2)
    # print(sorted(G.nodes()))
    # print(sorted(G.edges()))
    # nx.draw(G)
    # app = Viewer(G)
    # app.mainloop()

    G = M.toGraphvizGraph()
    s = G.string()
    print(s)
    G.layout()
    G.draw('graph.png')

    dfs(M, 0)
