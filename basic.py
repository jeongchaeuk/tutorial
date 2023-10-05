#!/usr/bin/python

"""Basic pygame program."""

import pygame
# from pygame.locals import *

def main():
    pygame.init()

    # font_size = 36
    # for name in pygame.font.get_fonts():
    #     font = pygame.font.SysFont(name, font_size)
    #     print(f"{name}={font.size('한')}")
    # font = pygame.font.Font(None, font_size)
    # print(f"{pygame.font.get_default_font()}={font.size('한')}")

    font_size = 36
    font_name = 'd2coding'
    font = pygame.font.SysFont(font_name, font_size)
    msg = 'Hello There'
    text_size = font.size(msg)
    print(text_size)

    screen_size = text_size[0]+100, text_size[1]+100
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Basic pygame program')

    background = pygame.Surface(screen.get_size()).convert()
    bgcolor = 'black'
    background.fill(bgcolor)

    font_color = 'yellow'
    text = font.render(msg, 1, font_color)
    text_pos = text.get_rect(centerx=background.get_rect().centerx)
    background.blit(text, text_pos)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    FPS = 60
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()

        clock.tick(FPS)
        # print(f'{clock.get_fps():.1f}')


if __name__ == '__main__':
    main()
