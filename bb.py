# bb.py
"""Boundce a ball sample"""

import sys, pygame

def main(width=1920, height=1080, speedx=10, speedy=10, fps=60):
    pygame.init()

    size = width, height
    print(size)
    speed = [speedx, speedy]

    bgcolor = 0, 0, 0 # black

    screen = pygame.display.set_mode(size, pygame.FULLSCREEN, vsync=1)
    clock = pygame.time.Clock()

    ball = pygame.image.load('intro_ball.gif').convert_alpha()
    ballrect = ball.get_rect()

    fps_range = [fps, 0]

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
        # print(f'{clock.get_fps():.1f}')
        if clock.get_fps():
            fps_range[0] = min(fps_range[0], clock.get_fps())
            fps_range[1] = max(fps_range[1], clock.get_fps())
        print(f'fps_range={fps_range}')

    pygame.quit()


if __name__ == '__main__':
    main(*[int(x) for x in sys.argv[1:]])
