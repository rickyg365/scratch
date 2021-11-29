import os
import time

from display_handler import Display
from maze_creator import Maze, print_matrix
from path_handler import graph_print, Graph, dijkstra_algorithm, apply_dijkstra


def main():
    os.system("cls")
    # Set row height and col width, respectively
    r = 20
    c = 40

    # Create random maze by initializing CreateMazeData object
    new_maze = Maze(r, c)

    # Export all data as a dict
    new_maze_data = new_maze.export_all_data()

    # Iterate and display data
    # for key, value in new_maze_data.items():
    #     # data attr's to skip
    #     matrix_keys = [
    #         "data",
    #         "occupied_data"
    #     ]
    #     # Special case
    #     if key in matrix_keys:
    #         print_matrix(value, f"{key} Cells")
    #         continue
    #     print(f"{key.capitalize()}:\n{value}\n")

    # returns a matrix with occupied and unoccupied squares
    occupied = new_maze_data["occupied_data"]

    start = new_maze_data["coord"][0]
    end = new_maze_data["coord"][1]

    start_key = f"{start[0]}_{start[1]}"
    end_key = f"{end[0]}_{end[1]}"
    # print(start_key, end_key)

    maze_graph = Graph(occupied)
    # graph_print(maze_graph.graph)  # 18, 38:  18_38 is last index

    # # Check Path
    # path_condition = has_path(maze_graph, start_key, end_key)
    # print("Path Found: ", path_condition)

    # # DFS
    # dfs_result = dfs_traversal(maze_graph, start_key)
    # print("\nDFS: ", dfs_result)

    # # BFS
    # bfs_result = bfs_traversal(maze_graph, start_key)
    # print("\nBFS: ", bfs_result)

    # Find Shortest Path

    # check if path is available first
    prev_nodes, shortest_path = dijkstra_algorithm(maze_graph, start_key)

    shortest_data = apply_dijkstra(prev_nodes, shortest_path, start_key, end_key)

    # print("\nShortest Path: ")  # , shortest_path
    # for k, v in shortest_data.items():
    #     print(f"  {k}: {v}")

    maze_display = Display(r, c)
    # 3 ways to access maze data, fix
    # 1. new_maze_data.export_all_data()["data"]
    # 2. new_maze_data["data"]
    # 3. new_maze_data()
    maze_display.insert_data(new_maze_data["data"])

    short_path = shortest_data["path"]

    if not short_path:
        print(maze_display)
    for spot in short_path[1:-1]:
        os.system("cls")
        spot_location = (int(x) for x in spot.split("_"))
        new_maze.update_maze_cell(spot_location, 3)
        maze_display.insert_data(new_maze.new_display_data)

        print(maze_display)
        time.sleep(.16)

    print("\nShortest Path: ")  # , shortest_path
    for k, v in shortest_data.items():
        if isinstance(v, list):
            print(f"  {k}: ")
            list_text = "    "
            count = 0
            for item in v:
                if count == 10:
                    count = 0
                    list_text += f"\n    {item:^6} "
                list_text += f"{item:^6} "
                count += 1
            print(list_text)
            continue
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
