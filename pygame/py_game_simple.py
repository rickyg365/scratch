import os
import pygame

from constants import WIDTH, HEIGHT


if __name__ == "__main__":
    pygame.init()
    FPS = 60  # Specififc to rendering and drawing game
    # Window Title
    pygame.display.set_caption("Quick Start")
    # CREATE WINDOW
    window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(pygame.Color('#000000'))

    is_running = True
    clock = pygame.time.Clock()
    while is_running:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"[ Mouse ]: {event}")


        window_surface.blit(background, (0, 0))

        pygame.display.update()

    pygame.quit()