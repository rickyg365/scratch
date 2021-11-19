from maze_creator import Maze, print_matrix
from simple_path import has_path, find_shortest_path, create_graph


def main():
    """
    Before the export data function we used display to see that it worked

    # Create new Display object, pass in (height, width) and insert maze data
    display = Display(r, c)
    display.insert_data(new_maze_data())

    # Show display
    print(display)
    """
    # Set row height and col width, respectively
    r = 20
    c = 40

    # Create random maze by initializing CreateMazeData object
    new_maze_data = Maze(r, c)

    # Export all data as a dict
    my_data = new_maze_data.export_all_data()

    # Iterate and display data
    for key, value in my_data.items():
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

    """
    all_data = {
            "coord": [self.start_coord, self.end_coord],
            "region": [self.start_region, self.end_region],
            "dimensions": [self.rows, self.cols],
            "data": self.new_display_data,
            "occupied_data": self.occupied_cells
    }
    """

    start = f"{my_data['coord'][0][0]}_{my_data['coord'][0][1]}"
    end = f"{my_data['coord'][1][0]}_{my_data['coord'][1][1]}"
    print(start)
    print(end)

    new_maze_graph = create_graph(my_data["occupied_data"], start, end)

    shortest_path = find_shortest_path(new_maze_graph, start, end)

    print(shortest_path)

    print("Found Path: ", has_path(new_maze_graph, start, end))


if __name__ == "__main__":
    main()
