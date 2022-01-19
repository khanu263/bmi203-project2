import networkx as nx
from search import graph

def test_bfs_traversal():

    # Create graph and make sure you can't start at a nonexistent node
    g = graph.Graph("data/tiny_network.adjlist")
    assert g.bfs("0") == None

    # For each starting point, compare my traversal implementation to
    # the BFS traversal created using networkx. The code for using
    # networkx for BFS traversal is derived from:
    #
    # https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.traversal.breadth_first_search.bfs_edges.html
    #
    for node in g.graph:
        traversal = g.bfs(node)
        nx_traversal = [node] + [v for u, v in nx.bfs_edges(g.graph, node)]
        assert traversal == nx_traversal

def test_bfs():

    # The first part of this test involves the following dummy graph
    # I made in data/dummy.adjlist:
    #
    #  A --> B --> C
    #        |     |
    #        |     |         F
    #        v     v
    #        E <-- D
    #
    g = graph.Graph("data/dummy.adjlist")
    assert len(g.bfs("A", end = "B")) == 2
    assert len(g.bfs("A", end = "C")) == 3
    assert len(g.bfs("A", end = "D")) == 4
    assert len(g.bfs("A", end = "E")) == 3
    assert g.bfs("A", end = "F") == None
    assert g.bfs("G", end = "A") == None

    # I then load in the citation network and test an unconnected node and a known path
    g = graph.Graph("data/citation_network.adjlist")
    assert g.bfs("34916529", end = "Nadav Ahituv") == None
    assert len(g.bfs("33637727", end = "34827709")) == 3