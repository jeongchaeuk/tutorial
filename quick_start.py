"""quick_start.py
    Example file showing a basic pygame *game loop*.
"""

import pygame

def main(width=1280, height=720, fps=60):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True
    delta_sec = 0
    move_per_seconds = 300
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() /2)

    # colors = list(pygame.color.THECOLORS.keys())
    # color_index = 0
    while running:
        for event in pygame.event.get():
            # close window
            if event.type == pygame.QUIT:
                running = False

        screen.fill('black')
        # screen.fill(colors[color_index])
        # color_index += 1
        # if color_index >= len(colors):
        #     color_index = 0

        #render your game here.
        pygame.draw.circle(screen, 'yellow', player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= move_per_seconds * delta_sec
        if keys[pygame.K_s]:
            player_pos.y += move_per_seconds * delta_sec
        if keys[pygame.K_a]:
            player_pos.x -= move_per_seconds * delta_sec
        if keys[pygame.K_d]:
            player_pos.x += move_per_seconds * delta_sec

        pygame.display.flip()

        # delta_sec is delta time in seconds since last frame, used for
        # framerate-independent physic.
        delta_sec = clock.tick(fps) / 1000

    pygame.quit()


if __name__ == '__main__':
    import sys
    main(*[int(x) for x in sys.argv[1:]])
