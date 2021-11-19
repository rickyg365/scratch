import os


class Node:
    location: tuple
    value: list


def adj_list_entry(current_coord, end_coord, dataset, visited=None, current_depth=0):
    if visited is None:
        visited = []

    height = len(dataset)
    width = len(dataset[0])

    start_row, start_col = current_coord
    print("current Coordinate: ", current_coord)
    # current_cell = dataset[start_row][start_col]
    """
    i-1 j
 i, j-1  i, j i,j+1
    i+1 j

    order: north east south west
    """
    neighbors = []

    if current_coord in visited:
        return
    visited.append(current_coord)

    d_row = [-1, 0, 1, 0]
    d_col = [0, 1, 0, -1]

    for i in range(4):
        current_row = start_row + d_row[i]
        current_col = start_col + d_col[i]

        # add boundary conditions and other checks here
        conditions = [
            current_row < 0,
            current_col < 0,
            current_row >= height,
            current_col >= width
        ]
        if any(conditions):
            continue

        if (current_row, current_col) in visited:
            continue

        # Ignore occupied spaces
        if dataset[current_row][current_col] == 1:
            continue

        # Found end
        # 1
        if (current_row, current_col) == end_coord:
            print("Ending Found!!!")

        new_neighbor = {
            "value": dataset[current_row][current_col],
            "location": (current_row, current_col)
        }
        neighbors.append(new_neighbor)
    print(f"{current_coord}: ", neighbors)
    return neighbors


def explore_neighbors(current_coord, dataset, visited=None):
    if visited is None:
        visited = []

    height = len(dataset)
    width = len(dataset[0])

    start_row, start_col = current_coord
    print("current Coordinate: ", current_coord)
    # current_cell = dataset[start_row][start_col]
    """
    i-1 j
 i, j-1  i, j i,j+1
    i+1 j
    
    order: north east south west
    """
    neighbors = []

    if current_coord in visited:
        return
    visited.append(current_coord)

    d_row = [-1, 0, 1, 0]
    d_col = [0, 1, 0, -1]

    for i in range(4):
        current_row = start_row + d_row[i]
        current_col = start_col + d_col[i]

        # add boundary conditions and other checks here
        conditions = [
            current_row < 0,
            current_col < 0,
            current_row >= height,
            current_col >= width
        ]
        if any(conditions):
            continue

        if (current_row, current_col) in visited:
            continue

        # Ignore occupied spaces
        if dataset[current_row][current_col] == 1:
            continue

        # Found end
        # 1
        if (current_row, current_col) == end_coord:
            print("Ending Found!!!")

        new_neighbor = {
            "value": dataset[current_row][current_col],
            "location": (current_row, current_col)
        }
        neighbors.append(new_neighbor)
    print(f"{current_coord}: ", neighbors)
    return neighbors


def bfs_find_path():
    pass


def dfs_find_path(current_coord, end_coord, dataset, visited=None, current_depth=0):  # current_coord, end_coord, dataset, visited=None, current_depth=0
    # visited_coord = []
    # start_depth = 0
    #
    # neighbors = explore_neighbors(
    #     current_coord=start_coord,
    #     end_coord=end_coord,
    #     dataset=data,
    #     visited=visited_coord,
    #     current_depth=start_depth
    # )
    #
    # for neigbor in neighbors:
    #     explore_neighbors(neigbor["location"], end_coord, data, )

    if visited is None:
        visited = []

    height = len(dataset)
    width = len(dataset[0])

    start_row, start_col = current_coord
    print("current Coordinate: ", current_coord)
    # current_cell = dataset[start_row][start_col]

    neighbors = []

    if current_coord in visited:
        return
    visited.append(current_coord)
    """ order: north east south west """
    d_row = [-1, 0, 1, 0]
    d_col = [0, 1, 0, -1]

    for i in range(4):
        current_row = start_row + d_row[i]
        current_col = start_col + d_col[i]

        # add boundary conditions and other checks here
        conditions = [
            current_row < 0,
            current_col < 0,
            current_row >= height,
            current_col >= width
        ]
        if any(conditions):
            continue

        if (current_row, current_col) in visited:
            continue

        # Ignore occupied spaces
        if dataset[current_row][current_col] == 1:
            continue

        # Found end
        # 1
        if (current_row, current_col) == end_coord:
            print(f"Ending Found!!! | [{end_coord}]")

        new_neighbor = {
            "value": dataset[current_row][current_col],
            "location": (current_row, current_col)
        }
        neighbors.append(new_neighbor)
        dfs_find_path(new_neighbor["location"], end_coord, dataset, visited, current_depth+1)
    print(f"{current_coord}[{current_depth}]: ", neighbors)
    return neighbors


def main():
    raw_data = [
        [1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, -1, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    start_coord = (1, 1)
    end_coord = (3, 1)

    # explore_neighbors(start_coord, end_coord, raw_data)
    dfs_find_path(start_coord, end_coord, raw_data)


if __name__ == "__main__":
    main()

