import os


def dfs_traversal(graph, source, order=None):
    if order is None:
        order = []
    # Stack
    """ Way #1 """
    # using stack

    # stack = [source]  # only use push and pop
    #
    # while len(stack) > 0:
    #     # remove last element from stack
    #     current = stack.pop()
    #     # what to do for each node
    #     print(current)
    #     # Add neighbor or connected nodes
    #     for node in graph[current]:
    #         stack.append(node)

    # what to do for each node

    """ Way #2 """
    # recursive
    order.append(source)
    print(source)
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
        order.append(current)
        print(current)

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


def main():
    sample_graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": []
    }

    dfs_result = dfs_traversal(sample_graph, "a")
    bfs_result = bfs_traversal(sample_graph, "a")
    path_result = has_path(sample_graph, "a", "f")

    print(f"Depth first: ", dfs_result)
    print(f"Breadth first: ", bfs_result)
    print(f"Path is available: ", path_result)


if __name__ == "__main__":
    main()
