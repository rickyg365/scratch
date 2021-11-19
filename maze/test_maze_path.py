from maze_creator import Maze, print_matrix
from path_handler import graph_print, has_path, create_graph, dfs_traversal, bfs_traversal, find_shortest_path


def main():
    # Set row height and col width, respectively
    r = 6
    c = 12

    # Create random maze by initializing CreateMazeData object
    new_maze = Maze(r, c)

    # Export all data as a dict
    new_maze_data = new_maze.export_all_data()

    # Iterate and display data
    for key, value in new_maze_data.items():
        # data attr's to skip
        matrix_keys = [
            "data",
            "occupied_data"
        ]
        # Special case
        if key in matrix_keys:
            print_matrix(value, f"{key} Cells")
            continue
        print(f"{key.capitalize()}:\n{value}\n")

    # returns a matrix with occupied and unoccupied squares
    occupied = new_maze_data["occupied_data"]

    start = new_maze_data["coord"][0]
    end = new_maze_data["coord"][1]

    start_key = f"{start[0]}_{start[1]}"
    end_key = f"{end[0]}_{end[1]}"
    print(start_key, end_key)

    maze_graph = create_graph(occupied)
    graph_print(maze_graph)  # 18, 38:  18_38 is last index

    # Check Path
    path_condition = has_path(maze_graph, start_key, end_key)
    print("Path Found: ", path_condition)

    # # DFS
    # dfs_result = dfs_traversal(maze_graph, start_key)
    # print("\nDFS: ", dfs_result)

    # # BFS
    # bfs_result = bfs_traversal(maze_graph, start_key)
    # print("\nBFS: ", bfs_result)

    # Find Shortest Path
    shortest_path = find_shortest_path(maze_graph, start_key, end_key)

    print("\nShortest Path: ")  # , shortest_path
    for k, v in shortest_path.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
