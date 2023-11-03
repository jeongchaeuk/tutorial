#!/usr/bin/env python

import pygame

def main():
    caption = 'Tutorial'

    pygame_display = pygame.display
    pygame_display.set_caption(caption)
    screen = pygame_display.set_mode(pygame_display.list_modes()[-1])
    screen.fill('whitesmoke')

    pygame_display_update = pygame_display.update
    clock = pygame.time.Clock()
    clock_tick = clock.tick
    pygame_event_get = pygame.event.get
    while 1:
        for event in pygame_event_get():
            match event.type:
                case pygame.QUIT:
                    return
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            return

        pygame_display_update()
        clock_tick(60)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
