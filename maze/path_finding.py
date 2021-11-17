import os


def explore_neighbors(current_coord, end_coord, dataset, visited=None):
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


def bfs_find_path():
    pass


def dfs_find_path():
    pass


def main():
    raw_data = [
        [1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, -1, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    start_coord = (1, 1)
    end_coord = (3, 1)

    explore_neighbors(start_coord, end_coord, raw_data)


if __name__ == "__main__":
    main()

