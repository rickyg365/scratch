import os

from dataclasses import dataclass
from typing import List, Optional


# @dataclass
# class Node:
#     value: int
#     location: tuple
#     neighbors: Optional[List]


def find_neighbors(cell, dataset):
    """ returns list of nodes that are neighbors """
    output_neighbors = []
    # Order: North East South West
    d_row = [-1, 0, 1, 0]
    d_col = [0, 1, 0, -1]

    for i in range(4):
        new_i = cell[0] + d_row[i]
        new_j = cell[1] + d_col[i]

        # New Node
        new_node = (new_i, new_j)
        output_neighbors.append(new_node)

    return output_neighbors


def create_graph(matrix, start, end):
    """ creates graph from starting point but ignores walls(cells == 1) """
    output_graph = {}

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            cell_key = f"{i}_{j}"
            output_neighbors = []
            # Order: North East South West
            d_row = [-1, 0, 1, 0]
            d_col = [0, 1, 0, -1]

            # if current cell value is occupied
            if f"{i}_{j}" == start or f"{i}_{j}" == end:
                cell = 2
            if cell == 1:
                continue

            # Get neighbors
            for x in range(4):
                new_i = i + d_row[x]
                new_j = j + d_col[x]

                new_location = (new_i, new_j)

                # Conditions
                border_conditions = [
                    new_i < 0,
                    new_j < 0,
                    new_j >= len(row),
                    new_i >= len(matrix)
                ]
                if any(border_conditions):
                    continue
                # if new cell is occupied
                if matrix[new_i][new_j] == 1:
                    continue

                # New Node
                # new_node = new_location
                output_neighbors.append(f"{new_i}_{new_j}")
            # add neighbors and key/node to adj list
            output_graph[cell_key] = output_neighbors

    return output_graph


def dfs_traversal(graph, source, order=None):
    if order is None:
        order = []
    # Stack
    # recursive
    if source in order:
        return

    order.append(source)
    # print(source)

    for node in graph[source]:
        dfs_traversal(graph, node,  order)

    return order


def bfs_traversal(graph, source, order=None):
    if order is None:
        order = []

    # Queue
    queue = [source]  # only use push and pop

    while len(queue) > 0:
        # Get first element
        current = queue.pop(0)

        if current in order:
            continue

        order.append(current)
        # print(current)

        for node in graph[current]:
            queue.append(node)

    return order


def has_path(graph, source, destination):
    """
    Way 1:

    # Base case
    if source == destination:
        return True

    for node in graph[source]:
        if has_path(graph, node, destination):
            return True
    return False

    """

    queue = [source]

    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node == destination:
            return True
        for node in graph[current_node]:
            queue.append(node)

    return False


def find_shortest_path(graph, source, end):
    visited = []
    queue = [source]
    num_queue = [0]
    tracker = {}
    infinitey = 99999

    while len(queue) > 0:
        # What to do with current node
        current_node = queue.pop(0)
        current_distance = num_queue.pop(0)
        # print(f"<{current_node}>: {current_distance}")
        #
        # if current_node == end:
        #     print("end", tracker[current_node][0])

        # Should only happen once
        if current_node == source:
            tracker[current_node] = [current_distance, ""]

        dist_to_neighbors = current_distance + 1
        for node in graph[current_node]:
            if node in visited:
                continue

            if tracker.get(node, None) is None:
                tracker[node] = [infinitey, ""]

            # what to do with neighbors
            if dist_to_neighbors < tracker[node][0]:
                tracker[node] = [dist_to_neighbors, current_node]

            queue.append(node)
            num_queue.append(dist_to_neighbors)

        visited.append(current_node)

    # Smallest Path
    smallest_dist = tracker[end][0]
    smallest_path = []

    # Build Path
    current = end

    while current != "":
        smallest_path.append(current)

        current = tracker[current][1]

    print(smallest_dist)
    return smallest_path


def mx_print(adj_list):
    output_text = ""

    for key, value in adj_list.items():
        output_text += f"{key}: {value}\n"

    print(output_text)


def convert_key(cell_key):
    return [int(x) for x in cell_key.split("_")]


def main():
    sample_graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": []
    }

    # dfs_traversal(sample_graph, "a")
    # bfs_traversal(sample_graph, "a")
    # print(f"Has Path: ", has_path(sample_graph, "a", "f"))

    sample_matrix = [
        [1, 2, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [-1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1]
    ]
    start_coord = "0_1"
    end_coord = "2_0"
    # start = 2
    # end = -1

    new_graph = create_graph(sample_matrix, (0, 1))
    # mx_print(new_graph)

    dfs_result = dfs_traversal(new_graph, start_coord)
    print("DFS: ", dfs_result)

    bfs_result = bfs_traversal(new_graph, start_coord)
    print("BFS: ", bfs_result)

    path_result = has_path(new_graph, start_coord, end_coord)
    print("\nFound Path: ", path_result)

    for key, value in new_graph.items():
        print(f"{key}: {value}")
        i, j = convert_key(key)
        print(f"Value: ", sample_matrix[i][j])


if __name__ == "__main__":
    # main()
    # start = 2
    # end = -1
    sample_matrix = [
        [1, 2, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, -1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_coord = "0_1"
    end_coord = "2_2"

    # (0, 1)
    new_graph = create_graph(sample_matrix, convert_key(start_coord))

    shortest_path = find_shortest_path(new_graph, start_coord, end_coord)

    print(shortest_path)

