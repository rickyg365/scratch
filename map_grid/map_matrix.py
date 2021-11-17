import os

from typing import List

file_to_open = "simple_map_sample.csv"

room_id_types = {
    "0": "start",
    "1": "neutral",
    "2": "fight",
    "3": "reward"
}

map_data = []

# csv to 2d matrix
with open(file_to_open) as raw_map:

    for line in raw_map:
        # Clean row and split into list[char]
        line_list = line.strip().split(",")
        print(line_list)
        # Storage for row_data
        row_data = []
        for char in line_list:
            new_char = room_id_types.get(char, None)

            row_data.append(new_char)

            print(char)
        map_data.append(row_data)

rows = len(map_data)
cols = len(map_data[0])

print(map_data)

# 2d matrix to adjacency list or adjacency matrix
start = None


def explore_neighbors(data, current_row, current_col, row_max, col_max, visited) -> List[tuple]:
    """
            | r-1 c |
      r c-1 | r   c | r c+1
            | r+1 c |
    """
    drow = [-1, 1, 0, 0]
    dcol = [0, 0, 1, -1]
    # order, if you zip these 2 list you get a tuple of the direction coordinates
    # UP: (-1, 0)
    # DOWN:(1, 0)
    # RIGHT:(0, 1)
    # LEFT: (0, -1)
    neighbors = []

    for _ in range(4):
        new_row = current_row + drow[_]
        new_col = current_col + dcol[_]

        if new_col < 0 or new_row < 0:
            continue
        if new_col > col_max or new_row > row_max:
            continue

        current_neighbor = data[new_row][new_col]

        if current_neighbor in visited:
            continue
        neighbors.append((new_row, new_col))

    return neighbors


already_visited = []
for i, row in enumerate(map_data):
    for j, col_value in enumerate(row):
        if col_value == "start":
            start = (i, j)
        print(f"{col_value} [{i}][{j}]")
        neighbors = explore_neighbors(map_data, i, j, rows, cols, already_visited)
        print(f"Neighbors: {neighbors}")


def main():
    pass


if __name__ == "__main__":
    main()
