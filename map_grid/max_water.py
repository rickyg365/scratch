import os

from typing import List

"""
Practice:

    Start with an Edge List and make Adjacency List and Adjacency Matrix

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Dont need data point just the position because height[i] would give us the position
#         list_size = len(height)
#         max_area = 0
#         visited_locations = []
        
#         for left in range(list_size):
#             for right in range(list_size):
#                 coord = (left, right)
                
#                 if coord in visited_locations or (right, left) in visited_locations:
#                     continue
                    
#                 # calculate area
#                 x_dist = abs(right - left)
#                 y_dist = min(height[left], height[right])
#                 current_area = x_dist * y_dist
                
#                 # Check if current area is greater than the max
#                 
#                 if current_area > max_area:
#                     max_area = current_area
                    
#                 # add location to visited
#                 visited_locations.append(coord)

        max_water = 0
        left = 0
        right = len(height) - 1
        
        while(left < right):
            left_height = height[left]
            right_height = height[right]
            
            # calculate area
            x_dist = abs(right - left)
            y_dist = min(left_height, right_height)
            
            current_water = x_dist * y_dist

            # Check if current area is greater than the max
            if current_water > max_water:
                max_water = current_water
            
            # change coordinates
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        
        return max_water
        
"""


def maxArea_adj_matrix(height: List[int]):
    adjacency_matrix = []
    max_area = {
        "value": 0,
        "location": None
    }

    for left in range(len(height)):
        new_row = []
        for right in range(len(height)):
            x_dist = abs(right - left)
            y_dist = min(height[left], height[right])
            current_area = x_dist * y_dist

            if current_area > max_area["value"]:
                max_area["value"] = current_area
                max_area["location"] = (left, right)

            new_row.append(current_area)
        adjacency_matrix.append(new_row)

    return adjacency_matrix, max_area


def maxArea(height: List[int]) -> int:
    max_water = 0
    left = 0
    right = len(height) - 1

    while left < right:
        left_height = height[left]
        right_height = height[right]

        # calculate area
        x_dist = abs(right - left)
        y_dist = right_height
        if left_height < right_height:
            y_dist = left_height

        current_water = x_dist * y_dist

        # Check if current area is greater than the max
        """ if comparison or max() func? """
        if current_water > max_water:
            max_water = current_water

        # change coordinates
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return max_water


if __name__ == "__main__":

    example1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    example2 = [1, 1]
    example3 = [4, 3, 2, 1, 4]
    example4 = [1, 2, 1]

    adj_matrix, area_dict = maxArea_adj_matrix(example3)

    text_row = ""
    for line in adj_matrix:
        for char in line:
            text_row += f"{char:^2} "
        text_row += "\n"

    print(text_row)

    print(f"Max Area: {area_dict['value']}, Location: {area_dict['location']}")

    print(f"Max Water: {maxArea(example3)}")
