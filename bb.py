# bb.py
"""Boundce a ball sample"""

import sys, pygame

def main(width=1280, height=720, speedx=5, speedy=5, fps=60):
    pygame.init()

    size = width, height
    print(size)
    speed = [speedx, speedy]

    bgcolor = 0, 0, 0 # black

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    ball = pygame.image.load('intro_ball.gif')
    ballrect = ball.get_rect()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        prevrect = ballrect
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(bgcolor, prevrect)
        screen.blit(ball, ballrect)
        pygame.display.flip()

        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main(*[int(x) for x in sys.argv[1:]])
