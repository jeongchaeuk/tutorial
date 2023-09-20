"""quick_start.py
    Example file showing a basic pygame *game loop*.
"""

import pygame

def main(width=1280, height=720, fps=60):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False

        screen.fill('black')

        #render your game here.

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    import sys
    main(*[int(x) for x in sys.argv[1:]])
