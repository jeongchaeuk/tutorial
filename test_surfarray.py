#!/usr/bin/env python

import pygame as pg
import numpy as np

def make_gradation_alpha(size, color=(0, 0, 0, 255), stage=0,
                         direction='horizontal', reverse=False):
    """direction = horizontal | vertical"""
    w, h = size
    surf = pg.Surface(size, pg.SRCALPHA)
    surf.fill(color)

    alpha = color[3]

    num = w if direction == 'horizontal' else h
    new_alpha = np.linspace(1, 0, num) if reverse else np.linspace(0, 1, num)

    if not stage:
        stage = num
    inv_stage = 1 / stage
    new_alpha = new_alpha // inv_stage * inv_stage
    new_alpha = (new_alpha * alpha).astype('uint8')

    if direction == 'horizontal':
        new_alpha = np.repeat(new_alpha[:, np.newaxis], [h], 1)
    else:
        new_alpha = np.repeat(new_alpha[np.newaxis, :], [w], 0)
    pg.surfarray.pixels_alpha(surf)[:] = new_alpha[:]
    return surf


def draw_gradation_alpha(size, color):
    _center = pg.Surface(size, pg.SRCALPHA)
    _center.fill(color)
    _left = make_gradation_alpha(size, color)
    _right = make_gradation_alpha(size, color, reverse=True)

    w, h = size
    surf = pg.Surface((w * 3, h), pg.SRCALPHA)
    surf.blit(_left, (0, 0))
    surf.blit(_center, (w, 0))
    surf.blit(_right, (w * 2, 0))

    return surf


# def make_gradation(w, h):
#     screen = pg.display.get_surface()
#     # w, h = screen.get_size()
#     surf = pg.Surface((w, h), pg.SRCALPHA)
#     surf.fill('darkblue')
#     # rgb = pg.surfarray.pixels3d(surf)
#     alpha = pg.surfarray.pixels_alpha(surf)
#     new_alpha = (np.arange(h)/h*255).astype('uint8')
#     # new_alpha = np.repeat(new_alpha[:,None], [w], 1)
#     new_alpha = np.repeat(new_alpha[None, :], [w], 0)
#     alpha[:] = new_alpha[:]
#     return surf


def main():
    caption = 'Tutorial'

    pg_display = pg.display
    pg_display.set_caption(caption)
    screen = pg_display.set_mode(pg_display.list_modes()[-1])

    image = pg.image.load('data\\title_bg.png')
    screen.blit(image, (0, 0))

    pg_display_update = pg_display.update
    clock = pg.time.Clock()
    clock_tick = clock.tick
    pg_event_get = pg.event.get

    size = (screen.get_width() // 3, screen.get_height() // 3)
    grad = draw_gradation_alpha(size, (0, 0, 0, 100))
    screen.blit(grad, grad.get_rect(center=screen.get_rect().center))
    # left_surf, center_surf, right_surf = draw_gradation_alpha(size, (0, 0, 0, 100))

    # screen_center = screen.get_rect().center

    # left_surf_rect = left_surf.get_rect(center=screen_center)
    # left_surf_rect.centerx -= size[0]
    # screen.blit(left_surf, left_surf_rect)

    # screen.blit(center_surf, center_surf.get_rect(center=screen_center))

    # right_surf_rect = right_surf.get_rect(center=screen_center)
    # right_surf_rect.centerx += size[0]
    # screen.blit(right_surf, right_surf_rect)

    while 1:
        for event in pg_event_get():
            match event.type:
                case pg.QUIT:
                    return
                case pg.KEYDOWN:
                    match event.key:
                        case pg.K_ESCAPE:
                            return

        pg_display_update()
        clock_tick(60)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
