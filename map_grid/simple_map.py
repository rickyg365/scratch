import os

from dataclasses import dataclass


"""
Practice making adjacency list and matrix

usually you start with and edge list

Edge list -> Adjacency List
Edge list -> Adjacency Matrix

"""


class Room:
    """
    room_id_types = {
        "0": "start",
        "1": "neutral",
        "2": "fight",
        "3": "reward"
    }
    """

    def __init__(self, new_room_id, new_room_type_id):
        self.room_id_types = {
            "": "empty",
            "0": "start",
            "1": "neutral",
            "2": "fight",
            "3": "reward"
        }

        self.room_id = new_room_id
        self.room_type_id = new_room_type_id
        self.room_type = None

        # Location
        self.r = -1
        self.c = -1

        # Neighbors
        self.north = None
        self.east = None
        self.south = None
        self.west = None

        # Assign room type using input room_type_id
        self.assign_type_by_id()

    def __str__(self):
        return f"[ {self.room_id} ]({self.r}, {self.c}): {self.room_type_id} -> {self.room_type}"

    def __repr__(self):
        # print("repr")
        return f"<{self.room_id} {self.room_type} ({self.r}, {self.c})>"

    def assign_type_by_id(self):
        self.room_type = self.room_id_types.get(self.room_type_id, None)

    def update_coordinates(self, new_row_num, new_col_num):
        self.r = new_row_num
        self.c = new_col_num


def load_custom_map_data(filepath="simple_map_sample.csv"):
    """ Loads map from a csv file """
    # list_rooms = []
    # dict_id_rooms = {}
    # dict_coord_rooms = {}
    #
    # occupied_data = []
    raw_data_matrix = []

    room_id = 1
    with open(input_file) as raw_map:
        for row_num, raw_row in enumerate(raw_map):
            # Clean and split row into a list
            row = raw_row.strip().split(",")

            # Used by occupied_data
            # data_row = []
            matrix_row = []

            for col_num, room_type_id in enumerate(row):
                # if empty, skip
                if room_type_id == "":
                    # # occupied_data
                    # data_row.append(0)
                    matrix_row.append(None)
                    continue

                # Generate new room
                new_room = Room(room_id, room_type_id)
                new_room.update_coordinates(row_num, col_num)

                # add new room to data structure of choice
                # list_rooms.append(new_room)
                # dict_id_rooms[room_id] = new_room
                # dict_coord_rooms[f"{row_num}_{col_num}"] = new_room

                # occupied_data
                # data_row.append(1)
                matrix_row.append(new_room)

                # Update room id
                room_id += 1
            # occupied_data.append(data_row)
            raw_data_matrix.append(matrix_row)
    # this does not include any empty rooms
    total_length = room_id - 1

    return raw_data_matrix


# Load csv data into matrix, or adjacency matrix
input_file = "simple_map_sample.csv"

map_data_matrix = load_custom_map_data(input_file)


# Convert raw_data into whatever form you want
"""
Raw Data:
    list_rooms
    dict_rooms(id)
    dict_rooms(coord)
    occupied_list
    data_matrix
"""


def explore_neighbors(matrix, current_room):
    """ given the current room and the data_matrix find neighbor objects and append them
     can low-key just use the coordinates """
    row_max = len(matrix)
    col_max = len(matrix[0])

    start_row = current_room.r
    start_col = current_room.c

    # UP: (-1, 0)
    # DOWN:(1, 0)
    # RIGHT:(0, 1)
    # LEFT: (0, -1)
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, 1, -1]

    neighbors = []
    # print("\nParent: ", matrix[start_x][start_y])

    for _ in range(4):
        new_row = start_row + d_row[_]
        new_col = start_col + d_col[_]

        # Boundary
        if new_col < 0 or new_row < 0:
            continue
        if new_col >= col_max or new_row >= row_max:
            continue

        # If neighbor is empty
        if matrix[new_row][new_col] is None:
            continue

        # print(f"Child {_}: ", matrix[new_row][new_col])
        neighbors.append(matrix[new_row][new_col])

    return neighbors


def raw_data_adj_list(data_matrix):
    new_adj_list = {}

    for row in data_matrix:
        for col_val in row:
            if col_val is None:
                continue
            neighbors = explore_neighbors(data_matrix, col_val)

            new_adj_list[col_val.room_id] = neighbors

    return new_adj_list


def raw_data_adj_matrix(data_matrix):
    new_adj_matrix = []
    starting_point = Room

    list_of_rooms = []
    for row in data_matrix:
        for col_val in row:
            print(col_val)
            list_of_rooms.append(col_val)
            if isinstance(col_val, Room) and col_val.room_type == "start":
                starting_point = col_val

    side_length = len(list_of_rooms)

    for i in range(side_length):
        new_matrix_row = []
        for j in range(side_length):
            new_matrix_row.append(0)

    print("Starting Point: ", starting_point.r, starting_point.c)

    return starting_point, new_adj_matrix


if __name__ == "__main__":
    # raw_data_adj_matrix(list_rooms)
    adj_list = raw_data_adj_list(map_data_matrix)
    adj_matrix = raw_data_adj_matrix(map_data_matrix)

    for room_ref_num, neighbor_list in adj_list.items():
        print("\nParent: ", room_ref_num)
        for neighbor in neighbor_list:
            print("child", neighbor)
