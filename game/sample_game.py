import os
import random

# class Event:
#     def __init__(self, title, event_type, description, icon_char):
#         self.type = event_type
#
#         self.title = title
#         self.description = description
#         self.icon = icon_char
#
#
# class FightEvent(Event):
#     def __init__(self):
#         # maybe also takes in a battle manager
#         # self.battle = BattleManager()
#         super().__init__(
#             title="Fight",
#             event_type="fight",
#             description="You got into a fight.",
#             icon_char="X"
#         )
#
#     def start_battle(self):
#         battling = True
#         while battling:
#             print("1st char turn")
#             print("2nd char turn")
#             print("Round done")
#
#
# class RewardEvent(Event):
#     def __init__(self):
#         super().__init__(
#             title="Reward",
#             event_type="reward",
#             description="You found a reward!",
#             icon_char=""
#         )
#
#     def give_reward(self):
#         return "sword (Future Item type object)"
#
#
# class NeutralEvent(Event):
#     def __init__(self):
#         super().__init__(
#             title="Neutral",
#             event_type="neutral",
#             description="You are doing great!",
#             icon_char=""
#         )
#
#     def show_text(self):
#         return "Neutral room text"


class MapTile:
    def __init__(self, text):
        self.action = text

        self.north = None
        self.east = None
        self.south = None
        self.west = None

        self.no_children = True

    def __str__(self):
        child1 = "" if self.north is None else "N"
        child2 = "" if self.east is None else "E"
        child3 = "" if self.south is None else "S"
        child4 = "" if self.west is None else "W"
        return f"{self.action} [{child1}{child2}{child3}{child4}]"

    def add_child(self, tile, direction):
        match direction:
            # 1 - north
            # 2 - east
            # 3 - south
            # 4 - west
            case 1:
                self.north = tile
            case 2:
                self.east = tile
            case 3:
                self.south = tile
            case 4:
                self.west = tile
        self.no_children = False

    def available_directions(self):
        available_list = []
        child_status = {
            1: self.north is None,
            2: self.east is None,
            3: self.south is None,
            4: self.west is None
        }

        for key, status in child_status.items():
            if status:
                available_list.append(key)

        return available_list


map_tiles = {
    "fight": "Fight insued",
    "neutral": "Nothing happened",
    "reward": "Here is an item"
}

fight_map_tile = MapTile(map_tiles["fight"])
neutral_map_tile = MapTile(map_tiles["neutral"])
reward_map_tile = MapTile(map_tiles["reward"])


class Map:
    def __init__(self, starting_tile=None):
        if starting_tile is None:
            starting_tile = MapTile("Start")

        self.starting_tile = starting_tile
        self.current_tile = self.starting_tile

        self.map_tiles = {
            1: starting_tile
        }

        # Map width and length
        """
        everytime you add a north-south add 1 to length
        
        everytime you add a east-west add 1 to width
        
        """

        self.map_length = 1

    def add_tile(self, tile, direction, selected_tile=None):
        if selected_tile is None:
            selected_tile = self.current_tile

        opposite_direction = {
            1: 3,
            2: 4,
            3: 1,
            4: 2
        }

        # Room ID
        new_room_id = list(self.map_tiles.keys())[-1] + 1

        self.map_tiles[new_room_id] = tile

        selected_tile.add_child(tile, direction)
        tile.add_child(selected_tile, opposite_direction[direction])

        self.map_length += 1

    def update_current(self, new_tile):
        self.current_tile = new_tile

    def build_random(self, max_num=100):
        # Choose random number(max: 100) or pre-selected number of map tiles
        num_tiles = random.randint(10, max_num)
        print(f"Random Number: {num_tiles}")
        # self.map_length = num_tiles

        map_tiles = {
            1: "[ FIGHT ] Fight ensued",
            2: "[ NEUTRAL ]Nothing happened",
            3: "[ REWARD ] Here is an item"
        }

        for i in range(num_tiles):
            # choose a random maptile type
            rand_map_num = random.randint(1, 3)
            # Create maptile
            new_map_tile = MapTile(map_tiles[rand_map_num])

            # Choose random direction of the 4
            # 1 - north
            # 2 - east
            # 3 - south
            # 4 - west
            possible_directions = self.current_tile.available_directions()

            r = random.choice(possible_directions)

            self.add_tile(new_map_tile, r)

            self.update_current(new_map_tile)

    def print_all_rooms(self, current_tile=None):
        visited_rooms = []
        for room_id, room in self.map_tiles.items():

            if room_id in visited_rooms:
                continue

            print(room)

            child_rooms = [
                room.north,
                room.east,
                room.south,
                room.west
            ]

            def check_child(room):
                not_empty = room is not None
                not_visited = room.room_id not in visited_rooms

                if not_empty and not_visited:
                    print(room)

            map(check_child, child_rooms)

            # for child in child_rooms:
            #     cond1 = child is not None
            #     cond2 = child.room_id not in visited_rooms
            #
            #     if cond1 and cond2:
            #         print(child)
            #
            # condition1 = room.north is not None
            # condition2 = room.east is not None
            # condition3 = room.south is not None
            # condition4 = room.west is not None
            #
            # not_visited = room_id not in visited_rooms
            #
            # if condition1 and not_visited:
            #     print(room.north)
            # if condition2 and not_visited:
            #     print(room.east)
            # if condition3 and not_visited:
            #     print(room.south)
            # if condition4 and not_visited:
            #     print(room.west)

            visited_rooms.append(room_id)
        # if current_tile is None:
        #     current_tile = self.starting_tile
        #     print(current_tile)
        #
        # if current_tile.no_children:
        #     print(current_tile)
        #     return
        #
        # condition1 = current_tile.north is not None
        # condition2 = current_tile.east is not None
        # condition3 = current_tile.south is not None
        # condition4 = current_tile.west is not None
        #
        # if condition1:
        #     self.print_all_rooms(current_tile.north)
        #     print(current_tile.north)
        # if condition2:
        #     self.print_all_rooms(current_tile.east)
        #     print(current_tile.east)
        # if condition3:
        #     self.print_all_rooms(current_tile.south)
        #     print(current_tile.south)
        # if condition4:
        #     self.print_all_rooms(current_tile.west)
        #     print(current_tile.west)


def main():
    print("[ running main ]")
    new_map = Map()
    new_map.build_random(25)
    print(f"Map Length: {new_map.map_length}")
    new_map.print_all_rooms()


if __name__ == "__main__":
    main()
