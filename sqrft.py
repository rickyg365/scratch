import os


def order(length, width, height):
    areas = [(length*width), (width*height), (height*length)]
    surface_area = (2 * length * width) + (2 * width * height) + (2 * height * length)

    # surface_area = 0
    #
    # for area in areas:
    #     surface_area += 2 * area

    extra = min(areas)

    return surface_area + extra


o = order(2, 3, 4)
print(o)
