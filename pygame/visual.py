import os
import pygame

# Size, constant variables capitalized
WIDTH, HEIGHT = 600, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Framerate
FPS = 60

# Importing Image
# Loaded in as surfaces use .blit(surface_obj, (x, y)) to draw onto screen
# image_var_name = pygame.image.load(os.path.join("folder_name", 'image.png'))
# Resize and rotate
# image_name = pygame.transform.scale(image_var_name, (new_X, new_y))
#              pygame.transform.rotate(thing_to_rotate, rotate_amount)
# Starting pygame
# pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sample Window Title")


def create_rects(surface, sz_list):
    color = BLACK

    current_x = 15
    current_y = HEIGHT
    x_spacing = 20

    standard_width = 15
    # Don't really need this list
    resulting_obj = []

    for size in sz_list:
        x = current_x
        y = HEIGHT - size - 10
        height = size

        new_rect = pygame.draw.rect(surface, color, pygame.Rect(x, y, standard_width, height))
        resulting_obj.append(new_rect)

        current_x += x_spacing

    return resulting_obj


def draw_window():
    WIN.fill(GREEN)
    size_list = [10, 20, 30, 40, 50, 100, 200, 300, 400, 500]

    new_list = create_rects(WIN, size_list)
    # print(new_list)

    pygame.display.update()


def main():
    """
    Main Loop
    - handle collisions
    - handle logic
    """

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        # Get list of events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
