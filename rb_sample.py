import pygame, sys
from pygame.locals import*

pygame.init()
pygame.display.set_caption("Controlling World Project")
myScreen = pygame.display.set_mode((640, 480))
# myScreen = pygame.display.set_mode((640, 480), flags=pygame.SCALED)

myTextFont = pygame.font.SysFont("나눔손글씨고딕아니고고딩", 32)
# myTextFont = pygame.font.SysFont("d2coding", 32)
# myText = myTextFont.render("Hello, Pygame!", False, 'red', 'green').convert()
myText = myTextFont.render("안녕, 파이게임!", 1, 'red', 'green').convert()
myTextArea = myText.get_rect()
myTextArea.center = myScreen.get_rect().center
fpsClock = pygame.time.Clock()
dx = 0
dy = 0
area = myScreen.get_rect()

FPS = 60
clock = pygame.time.Clock()

SPEED = 10
# pygame.key.set_repeat(1000//FPS)
# pygame.key.start_text_input()
# pygame.key.set_text_input_rect((0, 0, 200, 100))
# pygame.event.set_keyboard_grab(True)

while True:
    myTextArea.center = (area.centerx + dx, area.centery + dy)
    myScreen.fill('white')
    myScreen.blit(myText, myTextArea)

    moveRight = 0 #3
    moveDown = 0 #4

    pygame.event.pump()
    for event in pygame.event.get():
        print(event.dict)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == CLIPBOARDUPDATE:
            print(pygame.event.event_name(event.type))
        if event.type == TEXTEDITING:
            print(event.text, event.start, event.length)
        if event.type == TEXTINPUT:
            print(event.text)
        if event.type == KEYDOWN:
            print(pygame.key.name(event.key))
            if event.key == K_DOWN:
                moveDown = 1
            if event.key == K_UP:
                moveDown = -1
            if event.key == K_RIGHT:
                moveRight = 1
            if event.key == K_LEFT:
                moveRight = -1
            if event.key == K_ESCAPE:
                pygame.event.set_grab(False)
            if event.key == K_F1:
                pygame.event.set_grab(True)
        # if event.type == KEYDOWN:
        #     if event.key == K_DOWN:
        #         moveDown += 1
        #     if event.key == K_UP:
        #         moveDown -= 1
        #     if event.key == K_RIGHT:
        #         moveRight += 1
        #     if event.key == K_LEFT:
        #         moveRight -= 1
        #     if event.key == K_ESCAPE:
        #         pygame.event.set_grab(False)
        #     if event.key == K_F1:
        #         pygame.event.set_grab(True)
        # elif event.type == KEYDOWN: #5
        #     if event.key == K_DOWN:
        #         moveDown = 1
        #         moveRight = 0
        #     elif event.key == K_UP:
        #         moveDown = -1
        #         moveRight = 0
        #     elif event.key == K_RIGHT:
        #         moveDown = 0
        #         moveRight = 1
        #     elif event.key == K_LEFT:
        #         moveDown = 0
        #         moveRight = -1
    if abs(moveRight) > 1:
        print(f'moveRight={moveRight}')
    if abs(moveDown) > 1:
        print(f'moveDown={moveDown}')

    dx += SPEED * moveRight
    dy += SPEED * moveDown

    pygame.display.update()
    clock.tick(FPS)
