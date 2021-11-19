import os
import collections
import sys

"""
Generalized path/dfs/bfs 
"""


class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.graph = self.create_graph()
        self.nodes = self.get_list_nodes()

    def create_graph(self):
        """ creates graph from matrix but ignores walls(cells == 1) """
        output_graph = {}

        for i, row in enumerate(self.matrix):
            for j, cell in enumerate(row):
                cell_key = f"{i}_{j}"
                output_neighbors = []
                # Order: North East South West
                d_row = [-1, 0, 1, 0]
                d_col = [0, 1, 0, -1]

                # if current cell value is occupied
                # if f"{i}_{j}" == start or f"{i}_{j}" == end:
                #     cell = 2
                if cell == 1:
                    continue

                # Get neighbors
                for x in range(4):
                    new_i = i + d_row[x]
                    new_j = j + d_col[x]

                    # New Node
                    new_key = f"{new_i}_{new_j}"

                    # Conditions
                    border_conditions = [
                        new_i < 0,
                        new_j < 0,
                        new_j >= len(row),
                        new_i >= len(self.matrix)
                    ]
                    if any(border_conditions):
                        continue
                    # if new cell is occupied skip
                    if self.matrix[new_i][new_j] == 1:
                        continue

                    output_neighbors.append(new_key)
                # add neighbors and key/node to adj list
                output_graph[cell_key] = output_neighbors

        return output_graph

    def get_list_nodes(self):
        nodes = []
        for key in self.graph:
            nodes.append(key)
        return nodes

    def get_nodes(self):
        """ Returns the nodes of the graph. """
        return self.nodes

    def get_outgoing_edges(self, node):
        """ Returns the neighbors of a node. """
        # connections = []
        # for out_node in self.nodes:
        #     if self.graph[node].get(out_node, False) != False:
        #         connections.append(out_node)
        # return connections
        pass

    def value(self, node1, node2):
        """ Returns the value of an edge between two nodes. 1 for our case"""
        # return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    unvisited = graph.get_nodes()
    shortest_path = {}
    previous_nodes = {}

    infinitey = sys.maxsize

    # initialize tracker
    for node in unvisited:
        shortest_path[node] = infinitey

    shortest_path[start_node] = 0

    while unvisited:
        current_min_node = None
        for node in unvisited:
            if current_min_node is None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbors = []
        for neighbor in graph.graph[current_min_node]:
            tentative = shortest_path[current_min_node] + 1
            if tentative < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative
                previous_nodes[neighbor] = current_min_node
#
        unvisited.remove(current_min_node)

    return previous_nodes, shortest_path


def apply_dijkstra(previous_nodes, shortest_path, start, target):
    if previous_nodes.get(target, None) is None:

        print("Unable to find path!")
        error_data = {
            "distance": 0,
            "path": []
        }
        return error_data
    # Smallest Path
    smallest_dist = shortest_path[target]
    smallest_path = collections.deque()

    # Build Path
    node = target

    while node != start:
        smallest_path.appendleft(node)

        node = previous_nodes[node]

    smallest_path.appendleft(start)
    # smallest data
    smallest_data = {
        "distance": smallest_dist,
        "path": list(smallest_path)
    }

    return smallest_data


# def create_graph(matrix):
#     """ creates graph from matrix but ignores walls(cells == 1) """
#     output_graph = {}
#
#     for i, row in enumerate(matrix):
#         for j, cell in enumerate(row):
#             cell_key = f"{i}_{j}"
#             output_neighbors = []
#             # Order: North East South West
#             d_row = [-1, 0, 1, 0]
#             d_col = [0, 1, 0, -1]
#
#             # if current cell value is occupied
#             # if f"{i}_{j}" == start or f"{i}_{j}" == end:
#             #     cell = 2
#             if cell == 1:
#                 continue
#
#             # Get neighbors
#             for x in range(4):
#                 new_i = i + d_row[x]
#                 new_j = j + d_col[x]
#
#                 # New Node
#                 new_key = f"{new_i}_{new_j}"
#
#                 # Conditions
#                 border_conditions = [
#                     new_i < 0,
#                     new_j < 0,
#                     new_j >= len(row),
#                     new_i >= len(matrix)
#                 ]
#                 if any(border_conditions):
#                     continue
#                 # if new cell is occupied skip
#                 if matrix[new_i][new_j] == 1:
#                     continue
#
#                 output_neighbors.append(new_key)
#             # add neighbors and key/node to adj list
#             output_graph[cell_key] = output_neighbors
#
#     return output_graph
#

# def dfs_traversal(graph, source, order=None):
#     """ returns list of nodes in dfs order """
#     if order is None:
#         order = []
#
#     # recursive
#     if source in order:
#         return
#
#     order.append(source)
#     # print(source)
#
#     for node in graph[source]:
#         dfs_traversal(graph, node,  order)
#
#     return order
#
#
# def bfs_traversal(graph, source, order=None):
#     """ returns list of nodes in bfs order """
#     if order is None:
#         order = []
#
#     # Queue
#     queue = [source]  # only use push and pop
#
#     while len(queue) > 0:
#         # Get first element
#         current = queue.pop(0)
#
#         if current in order:
#             continue
#
#         order.append(current)
#
#         for node in graph[current]:
#             queue.append(node)
#
#     return order
#
#
# def has_path(graph, source, destination):
#     """
#     Way 1:
#
#     # Base case
#     if source == destination:
#         return True
#
#     for node in graph[source]:
#         if has_path(graph, node, destination):
#             return True
#     return False
#
#     """
#
#     queue = [source]
#
#     while len(queue) > 0:
#         current_node = queue.pop(0)
#         if current_node == destination:
#             return True
#         for node in graph[current_node]:
#             queue.append(node)
#
#     return False
#
#
# def find_shortest_path(graph, source, end):
#     """ returns dict with smallest distance and path """
#     visited = []
#     queue = [source]
#     num_queue = [0]
#     tracker = {}
#     infinitey = 99999
#
#     tracker[source] = [0, ""]
#
#     while len(queue) > 0:
#         print(queue)
#         print(len(queue), sep="\r")
#         # What to do with current node
#         current_node = queue.pop(0)
#         current_distance = num_queue.pop(0)
#         # print(f"<{current_node}>: {current_distance}")
#
#         # all neighbor nodes have same distance since they all only add 1 to distance
#         dist_to_neighbors = current_distance + 1
#         neighbors = []
#         list_of_short_dist = []
#         for node in graph[current_node]:
#             if node in visited:
#                 continue
#
#             # if node not in tracker add with default state
#             if tracker.get(node, None) is None:
#                 tracker[node] = [infinitey, ""]
#
#             # what to do with neighbors
#             if dist_to_neighbors < tracker[node][0]:
#                 tracker[node] = [dist_to_neighbors, current_node]
#
#             this_shortest = tracker[node][0]
#             neighbors.append(node)
#             list_of_short_dist.append(this_shortest)
#             num_queue.append(dist_to_neighbors)
#
#         # Go by smallest first
#
#         for neighbor in neighbors:
#             shortest = min(list_of_short_dist)
#             chosen_index = list_of_short_dist.index(shortest)
#             queue.append(neighbors[chosen_index])
#             neighbors.remove(neighbors[chosen_index])
#             list_of_short_dist.remove(shortest)
#         visited.append(current_node)
#
#     # Smallest Path
#     smallest_dist = tracker[end][0]
#     smallest_path = []
#
#     # Build Path
#     current = end
#
#     while current != "":
#         smallest_path.append(current)
#
#         current = tracker[current][1]
#
#     # smallest data
#     smallest_data = {
#         "distance": smallest_dist,
#         "path": smallest_path
#     }
#     return smallest_data


def graph_print(adj_list):
    output_text = "Graph:\n"

    for key, value in adj_list.items():
        output_text += f"  {key}: {value}\n"

    print(output_text)


def convert_key(cell_key):
    return [int(x) for x in cell_key.split("_")]


def main():
    sample_matrix = [
        [1, 2, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, -1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_coord = "0_1"
    end_coord = "2_2"

    # Convert matrix into graph
    final_graph = Graph(sample_matrix)

    # print(new_node_list)
    print(final_graph.graph)

    prev_nodes, short_path = dijkstra_algorithm(final_graph, start_coord)

    output_data = apply_dijkstra(prev_nodes, short_path, start_coord, end_coord)

    print("Shortest Path: ")
    for k, v in output_data.items():
        print(f"  {k}: {v}")

    # # Check Path
    # path_condition = has_path(new_graph, start_coord, end_coord)
    # print("Path Found: ", path_condition)
    #
    # # DFS
    # dfs_result = dfs_traversal(new_graph, start_coord)
    # print("\nDFS: ", dfs_result)
    #
    # # BFS
    # bfs_result = bfs_traversal(new_graph, start_coord)
    # print("\nBFS: ", bfs_result)
    #
    # # Find Shortest Path
    # shortest_path = find_shortest_path(new_graph, start_coord, end_coord)
    #
    # print("\nShortest Path: ")  # , shortest_path
    # for k, v in shortest_path.items():
    #     print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
