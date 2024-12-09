import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running =  True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()

        # FPS 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
