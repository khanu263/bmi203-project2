from turtle import back
import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and 
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None

        """

        # Make sure start and end nodes are in the graph
        if start not in self.graph:
            return None
        if end and end not in self.graph:
            return None

        # Initialize tracking structures
        visited = [start]
        queue = [start]
        traversal = []

        # If we're looking for a path, we need to track parents too
        if end:
            backtrack = {}

        # Keep going until the queue is empty
        while len(queue) > 0:

            # Pop the start of the queue, add it to traversal, and get its non-visited neighbors
            popped = queue.pop(0)
            traversal.append(popped)
            to_visit = [i for i in self.graph.neighbors(popped) if i not in visited]

            # Go through each unvisited neighbor
            for node in to_visit:

                # Add it to the queue and mark it as visited
                queue.append(node)
                visited.append(node)

                # If we're looking for a shortest path, keep track of the parent node,
                # and if this is the desired node, reconstruct the path to the start
                if end:
                    backtrack[node] = popped
                    if node == end:
                        path = [node]
                        while node != start:
                            node = backtrack[node]
                            path.insert(0, node)
                        return path

        # If there's an end node and we haven't returned yet, there's no path
        if end:
            return None
        
        # If there isn't an end node, return the full traversal
        return traversal