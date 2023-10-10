#!/usr/bin/env python
"""HP bar"""

# import sys

import pygame

pygame.init()

pygame.display.set_caption('Red/Black project')
SCREEN_W = 640
SCREEN_H = 480
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.SCALED)
print(f'window_size= {pygame.display.get_window_size()}')
print(f'screen.get_rect= {screen.get_rect()}')

screen.fill('gray')
pygame.display.flip()

MAX_HP = 10
FONT_SIZE = 32
font = pygame.font.SysFont('d2coding', FONT_SIZE)
clock = pygame.time.Clock()
text_area = (font.render(f'{MAX_HP}/{MAX_HP}', True, 'red')
             .get_rect(center=screen.get_rect().center))
FPS = 60
# pygame.key.set_repeat(1000 // FPS)

def main():
    HP = 5
    # digit = len(str(MAX_HP))
    pushed = [False, False]
    boards = make_boards()
    most_color = get_most_color(boards)

    while True:
        # msg = f'{HP:{digit}d}/{MAX_HP:{digit}d}'
        # text = font.render(msg, True, 'red').convert_alpha()
        # screen.fill('gray', text_area)
        # screen.blit(text, text_area)
        
        # update_area = [text_area]
        update_area = []
        update_area.append(drawHP(HP))
        update_area += (btn_rects := draw_buttons(pushed))
        update_area.append(draw_boards(boards))
        pygame.display.update(update_area)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.key.set_repeat()
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    HP = increase_hp(HP)
                elif event.key == pygame.K_DOWN:
                    HP = decrease_hp(HP)
                elif event.key == pygame.K_r:
                    boards = make_boards()
                    most_color = get_most_color(boards)
            elif event.type == pygame.MOUSEBUTTONUP:
                pushed = [False, False]
                x, y = event.pos
                pick_color = ''
                if btn_rects[0].collidepoint(x, y):
                    pick_color = 'red'
                elif btn_rects[1].collidepoint(x, y):
                    pick_color = 'gray25'
                else:
                    continue
                
                if pick_color == most_color:
                    HP = increase_hp(HP)
                else:
                    HP = decrease_hp(HP)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if btn_rects[0].collidepoint(x, y):
                    pushed = [True, False]
                elif btn_rects[1].collidepoint(x, y):
                    pushed = [False, True]

        clock.tick(FPS)


def increase_hp(hp):
    return hp + 1 if hp < MAX_HP else MAX_HP


def decrease_hp(hp):
    return hp - 1 if hp > 0 else 0


def make_boards():
    import random

    colors = ['red', 'gray25']
    rows = cols = 5
    return ([[random.choice(colors) for c in range(cols)] for r in range(rows)])


def get_most_color(boards):
    from collections import Counter
    counter = Counter()
    for r in boards:
        for c in r:
            counter[c] += 1
    return counter.most_common(1)[0][0]


def draw_boards(boards):
    size = 50
    rows = cols = 5
    screen_size = screen.get_rect().size
    x = (screen_size[0] - cols * size) // 2
    y = (screen_size[1] - rows * size) // 2

    for r in range(rows):
        for c in range(cols):
            pygame.draw.rect(screen, 
                             boards[r][c],
                             (x + c * size, y + r * size, size, size))
    width = 4
    correct = width // 2
    for r in range(1, rows):
        start_pos = (x, y + r * size)
        end_pos = (start_pos[0] + size * cols - correct, start_pos[1])
        pygame.draw.line(screen, 'whitesmoke', start_pos, end_pos, width)

    for c in range(1, cols):
        start_pos = (x + c * size, y)
        end_pos = (start_pos[0], start_pos[1] + size * rows - correct)
        pygame.draw.line(screen, 'whitesmoke', start_pos, end_pos, width)

    return pygame.draw.rect(screen, 'whitesmoke', (x, y, cols * size, rows * size), width)
    # return (x, y, cols * size, rows * size)


def drawHP(hp):
    bar = pygame.rect.Rect(20, 20, 20, (screen.get_rect().h - 40) // MAX_HP)
    pygame.draw.rect(screen, 'gray',
                     (bar.x, bar.y, bar.w, bar.h * (MAX_HP - hp)))
    pygame.draw.rect(screen, 'blue',
                     (bar.x, bar.y + bar.h * (MAX_HP - hp), bar.w, bar.h * hp))
    for i in range(MAX_HP):
        pygame.draw.rect(screen, 'whitesmoke',
                         (bar.x, bar.y + i * bar.h, bar.w, bar.h), width=2)
    bar.h *= MAX_HP
    return bar


def draw_buttons(pushed):
    screen_size = screen.get_rect().size
    size = 50
    gap = 10
    x = (screen_size[0] - size * 2 - gap) / 2
    y = screen_size[1] - size - screen_size[1] * 0.05

    rects = []
    rects.append(draw_button('red', (x, y, size, size), pushed[0]))
    rects.append(draw_button('gray25', (x + size + gap, y, size, size), pushed[1]))
    return rects


def draw_button(color, rect, pushed):
    rect = pygame.draw.rect(screen, color, rect)
    darker = pygame.Color(color).lerp('black', .5)
    lighter = pygame.Color(color).lerp('whitesmoke', .5)
    if pushed:
        darker, lighter = lighter, darker
    width = 4
    correct = width // 2
    pygame.draw.line(screen, darker,
                     (rect.left, rect.bottom-correct),
                     (rect.right, rect.bottom-correct), width)
    pygame.draw.line(screen, darker,
                     (rect.right-correct, rect.top),
                     (rect.right-correct, rect.bottom), width)
    correct = (width - 1) // 2
    pygame.draw.line(screen, lighter,
                     (rect.left, rect.top+correct),
                     (rect.right, rect.top+correct), width)
    pygame.draw.line(screen, lighter,
                     (rect.left+correct, rect.top),
                     (rect.left+correct, rect.bottom), width)
    return rect


if __name__ == '__main__':
    main()
