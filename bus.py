import os
import random

"""
Program: Bus Manager
Author: rickyg3
Date: 04/11/21
"""

'''
Passenger:
    name, type, departure, arrival
    
Stop:
    name, type
    
Route:
    start, end, rest_stops
    
Bus:
    name, id, route, break_stops, 
    
for now use predefined route but maybe try to write an algorithim that can find potential routes based 
    on a start and end station and what stations each station can go to
    
routes = [
    ["LA", "Indio", "AZ"],
    ["LA", "Kettleman City/Avenal", "SF"],
    ["Santa Monica", "Union Station", "Montclair"]
]
'''


def find_route(start, end):
    routes = [
        # {"LA": "regular", "Indio": "rest" , "AZ": "regular"}
        # {"LA": 1, "Indio": 0 , "AZ": 1}
        # {"LA": [10010], "Indio": [00010] , "AZ": [10010]}   >>> [regular(1) or rest(0), ]

        ["LA", "Ontario", "Indio", "AZ"],
        ["LA", "Kettleman City/Avenal", "SF"],
        ["Santa Monica", "Union Station", "Montclair"]
    ]

    for route in routes:
        condition1 = start.lower() == route[0].lower()
        condition2 = end.lower() == route[-1].lower()
        if condition1 and condition2:
            return route
    print("NO matching routes...")
    return None


class Passenger:
    def __init__(self, passenger_name, ticket_type, departure_station, arrival_station):
        self.name = passenger_name
        self.type = ticket_type
        self.departure = departure_station
        self.arrival = arrival_station
        self.route = None

    def __str__(self):
        text = f"\n{self.name}\t \t[{self.type}]"
        text += f"\nDeparture Station: {self.departure}"
        text += f"\nArrival Station: {self.arrival}"
        return text


class Stop:
    """
    stop_types = [
            "rest",
            "station",
    ]
    """
    def __init__(self, stop_name="", stop_type=""):
        self.name = stop_name
        self.type = stop_type

        self.prev = None
        self.next = None

    def __str__(self):
        text = f"{self.name}: [{self.type}]"
        return text


class Route:
    def __init__(self):

        self.rest_stops = []
        self.route_head = None
        self.route_tail = None

    def __str__(self):
        text = ""
        return text

    def add_stop(self, stop_name="", stop_type=""):
        new_stop = Stop(stop_name, stop_type)
        if stop_type == 'rest':
            self.rest_stops.append(new_stop)
        if self.route_tail:
            # connect previous tail to new tail
            self.route_tail.next = new_stop
            # connect for backwards compatibility
            new_stop.prev = self.route_tail
            # Update tail
            self.route_tail = new_stop
        else:
            self.route_head = new_stop
            self.route_tail = new_stop

    def kth_stop(self, k_stop=0):
        pass
    # def find_route(self, start, end):
    #     routes = [
    #         ["LA", "Indio", "AZ"],
    #         ["LA", "Kettleman City/Avenal", "SF"],
    #         ["Santa Monica", "Union Station", "Montclair"]
    #     ]
    #
    #     for route in routes:
    #         condition1 = start.lower() == route[0].lower()
    #         condition2 = end.lower() == route[-1].lower()
    #         if condition1 and condition2:
    #             self.rest_stops = route[1]
    #             return route
    #     print("NO matching routes...")
    #     return False


class Bus:
    def __init__(self, bus_name):
        self.name = bus_name
        self.id = "#042"
        # Passengers
        self.passengers = []
        # Linked list? or should we just do a list of all stops in order
        self.route = None
        # Name of break stops
        self.break_stops = None

    def __str__(self):
        # Header
        text = f"\n.{'-'* (len(self.name) + 5 + len(self.id))}."
        text += f"\n| {self.name.title()} [{self.id}] |"
        text += f"\n'{'-' * (len(self.name) + 5 + len(self.id))}'"
        # Body
        text += f"\nRoute: {self.route}"
        for passen in self.passengers:
            text += f"\n{passen}"
        # Footer
        text += f"\n"
        return text

    def add_passenger(self, passenger_object):
        self.passengers.append(passenger_object)
        # Make a personal route for each

    def add_route(self, start_location, end_location):
        # Create Route
        new_route = find_route(start_location, end_location)
        # Assign to Bus class variables
        self.route = new_route
        # self.break_stops =

    def make_json(self):
        temp_json = {}
        # make passengers and route json
        temp_json[f"{self.name}"] = {"passengers": self.passengers, "route": self.route}


if __name__ == "__main__":
    loc1 = "LA"
    loc2 = "AZ"

    my_bus = Bus("local bus")
    my_bus.add_route(loc1, loc2)

    # Create passengers
    pas1 = Passenger("fake_name", "first class", "LA", "AZ")
    pas2 = Passenger("fake_name", "economy", "Indio", "AZ")
    pas3 = Passenger("fake_name", "worker", "LA", "Indio")
    pas4 = Passenger("fake_name", "business class", "LA", "AZ")

    my_bus.add_passenger(pas1)
    my_bus.add_passenger(pas2)
    my_bus.add_passenger(pas3)
    my_bus.add_passenger(pas4)

    print(my_bus)
