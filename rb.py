#!/usr/bin/env python
"""Red block & Blak block."""

import pygame

class MyText(pygame.sprite.DirtySprite):
    _dx, _dy = 10, 10

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.visible = 1
        self.dirty = 2

    def update(self):
        self.rect = self.calc_newpos()

    def calc_newpos(self):
        newpos = self.rect.move(self._dx, self._dy)
        area = pygame.display.get_surface().get_rect()

        if not area.contains(newpos):
            if newpos.left < 0 or newpos.right > area.right:
                self._dx = -self._dx
            if newpos.top < 0 or newpos.bottom > area.bottom:
                self._dy = -self._dy
            newpos = self.rect.move(self._dx, self._dy)

        return newpos


def draw_text():
    SCREEN_SIZE = (640, 480)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    # screen = pygame.display.set_mode(SCREEN_SIZE, flags=pygame.SCALED, vsync=1)
    pygame.display.set_caption('Hello World Project')

    background = pygame.Surface(screen.get_size()).convert()
    background.fill('black')

    font = pygame.font.SysFont('d2coding', 32)
    mytext = MyText(font.render('안녕!', True, 'red', 'green').convert())
    group0 = pygame.sprite.LayeredDirty(mytext)

    FPS = 60
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # group0.clear(screen, background)
        group0.update()
        rect_list = group0.draw(screen, background)
        # print(rect_list)
        # pygame.display.update(rect_list)
        pygame.display.flip()
        clock.tick(FPS)


def main():
    pygame.init()
    draw_text()
    pygame.quit()


if __name__ == '__main__':
    main()
