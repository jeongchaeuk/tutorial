#!/usr/bin/env python
#
# Tom's Pong
# A simple pong game with realistic physics and AI.
# http://tomchance.org.uk/projects/pong
#
# Released under the GNU General Public License

# import getopt
import math
import os

import pygame

# import random
# import sys
# from socket import *

# from pygame.locals import *

VERSION = '0.4'


def load_png(name):
    """Load image and return image object."""

    fullname = os.path.join('.\\data', name)
    try:
        image = pygame.image.load(fullname)
        # If no display mode has been set,
        # program has terminated when call convert(). why??
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError as e:
        print(f'Cannot load image: {fullname}, {e}')
        raise SystemExit from e

    return image, image.get_rect()


class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen.
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector, *players):
        super().__init__()
        self.vector = vector
        self.players = players
        self.image, self.rect = load_png('pong_ball.png')
        screen = pygame.display.get_surface()
        assert screen is not None
        self.area = screen.get_rect()
        self.hit = False # is collided by bat?

    def update(self):
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos
        radian, speed = self.vector

        if not self.area.contains(newpos):
            tl = not self.area.collidepoint(newpos.topleft)
            tr = not self.area.collidepoint(newpos.topright)
            bl = not self.area.collidepoint(newpos.bottomleft)
            br = not self.area.collidepoint(newpos.bottomright)
            if (tl and tr) or (bl and br):
                radian = -radian
            if tl and bl:
                #self.offcourt()
                radian = math.pi - radian
            if tr and br:
                #self.offcourt()
                radian = math.pi - radian
        else:
            # Deflate the rectangle,
            # so you can't catch a ball behind the bat.
            self.players[0].rect.inflate(-3, -3)
            self.players[1].rect.inflate(-3, -3)

            # Do ball and bat collide?
            if self.hit:
                self.hit = False
            elif -1 != self.rect.collidelist([self.players[0].rect,
                                              self.players[1].rect]):
                radian = math.pi - radian
                self.hit = True

        self.vector = (radian, speed)

    def calcnewpos(self, rect, vector):
        """Calculate new position."""
        rad, spd = vector
        return rect.move(round(spd * math.cos(rad)), 
                         round(spd * math.sin(rad)))


class Bat(pygame.sprite.Sprite):
    """Movable tennis 'bat' with which one hits the ball.
    Returns: bat object
    Functions: reinit, update, moveup, movedown
    Attributes: which, speed"""

    def __init__(self, side):
        super().__init__()
        self.image, self.rect = load_png('pong_bat.png')
        screen = pygame.display.get_surface()
        assert screen is not None
        self.area = screen.get_rect()
        self.side = side
        self.speed = 10
        self.state = 'still'
        self.movepos = [0, 0]
        self.reinit()

    def reinit(self):
        self.movestop()
        if self.side == 'left':
            self.rect.midleft = self.area.midleft
        elif self.side == 'right':
            self.rect.midright = self.area.midright

    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pygame.event.pump()

    def moveup(self):
        self.movepos[1] -= self.speed
        self.state = 'moveup'

    def movedown(self):
        self.movepos[1] += self.speed
        self.state = 'movedown'

    def movestop(self):
        self.state = 'still'
        self.movepos = [0, 0]


def main():
    pygame.init()
    # Initialize screen
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Basic Pong')

    # Fill background
    background = pygame.Surface(screen.get_size()).convert()
    background.fill('black')

    # Initialize players
    player1 = Bat('left')
    player2 = Bat('right')

    # Initialize ball
    BALL_SPEED = 10
    RAD = 0.47
    # rand = ((0.1 * (random.randint(5,8))))
    ball = Ball((RAD, BALL_SPEED), player1, player2)

    # Initialize  sprites
    players = pygame.sprite.RenderPlain(player1, player2)
    balls = pygame.sprite.RenderPlain(ball)

    # Blit everything to the screen.
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialize clock
    FPS = 60
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player1.moveup()
                if event.key == pygame.K_z:
                    player1.movedown()
                if event.key == pygame.K_UP:
                    player2.moveup()
                if event.key == pygame.K_DOWN:
                    player2.movedown()
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_a, pygame.K_z):
                    player1.movestop()
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    player2.movestop()

        # screen.blit(background, ball.rect)
        # screen.blit(background, player1.rect)
        # screen.blit(background, player2.rect)
        balls.clear(screen, background)
        players.clear(screen, background)

        balls.update()
        players.update()

        balls.draw(screen)
        players.draw(screen)

        pygame.display.flip()

        # Make sure game run in 60 fps.
        clock.tick(FPS)


if __name__ == '__main__':
    main()
