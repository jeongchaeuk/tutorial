"""mychimp.py"""

import os
import pygame as pg

if not pg.font:
    print('Warning: fonts disabled.')
if not pg.mixer:
    print('Warning: sound disabled.')

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')
print(f'main_dir={main_dir}')
print(f'data_dir={data_dir}')


def load_image(name, colorkey=None, scale=1):
    """load image"""
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)
    size = image.get_size()

    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    image = image.convert()

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    """load sound"""
    class NoneSound:
        """NoneSound class"""
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
    sound = pg.mixer.Sound(fullname)
    return sound


class Fist(pg.sprite.Sprite):
    """Moves a clenched fist on the screen. Following the mouse."""

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('fist.png', -1)
        self.fist_offset = (-235, -80)
        self.punching = False

    def update(self):
        """Move the fist base on the mouse position."""
        pos = pg.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.fist_offset)
        if self.punching:
            self.rect.move_ip(15, 25)

    def punch(self, target):
        """Return true if the fist collides with the target."""
        if not self.punching:
            self.punching = True
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        """Called to pull the fist back."""
        self.punching = False


class Chimp(pg.sprite.Sprite):
    """Moves the monkey critter across the screen.
    It can spin the monkey when it is punched."""

    def __init__(self) -> None:
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('chimp.png', -1, 4)
        self.original = self.image
        self.rect.topleft = 10, 90
        self.move = 2
        self.dizzy = False
        screen = pg.display.get_surface()
        self.area = screen.get_rect()

    def speedup(self, up):
        new_move = abs(self.move)
        if up:
            new_move = min(60, new_move + 2)
        else:
            new_move = max(2, new_move - 2)

        self.move = new_move if self.move > 0 else -new_move
        print(self.move)

    def update(self):
        """Walk or spin, depending on the monkey's state."""
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def punched(self):
        """This will cause the monkey to start spinning."""
        if not self.dizzy:
            self.dizzy = True
            self.original = self.image

    def _walk(self):
        """Move the monkey across the screen, and turn at the ends."""
        newpos = self.rect.move((self.move, 0))
        if not self.area.contains(newpos):
            if (self.rect.left < self.area.left or
                self.area.right < self.rect.right):
                self.move = -self.move
                newpos = self.rect.move((self.move, 0))
                self.image = pg.transform.flip(self.image, True, False)
        self.rect = newpos

    def _spin(self):
        """Spin the monkey image."""
        center = self.rect.center
        self.dizzy += 12
        if self.dizzy >= 360:
            self.dizzy = False
            self.image = self.original
        else:
            rotate = pg.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)


def main():
    """main"""
    pg.init()
    screen = pg.display.set_mode((1280, 400), pg.SCALED)
    pg.display.set_caption('Monkey Fever')
    # pg.mouse.set_visible(False)

    BG_COLOR = (170, 238, 187)
    background = pg.Surface(screen.get_size()).convert()
    background.fill(BG_COLOR)

    if pg.font:
        # font = pg.sysfont.SysFont('d2coding', 64)
        # text = font.render('원숭이를 잡아 돈을 획득.', True, (10, 10, 10))
        # text = font.render('Pummel The Chimp, And Win $$$', True, (10, 10, 10), BG_COLOR)
        font = pg.font.Font(None, 64) # default font is `freesansbold`.
        text = font.render('Pummel The Chimp, And Win $$$', True, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
        background.blit(text, textpos)

    whiff_sound = load_sound('whiff.wav')
    punch_sound = load_sound('punch.wav')
    chimp = Chimp()
    fist = Fist()
    allsprites = pg.sprite.RenderPlain((chimp, fist))
    clock = pg.time.Clock()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    chimp.speedup(True)
                    punch_sound.play()
                    chimp.punched()
                else:
                    chimp.speedup(False)
                    whiff_sound.play() # miss
            elif event.type == pg.MOUSEBUTTONUP:
                fist.unpunch()

        allsprites.update()

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pg.display.flip()
        clock.tick(60)

    pg.quit()


if __name__ == '__main__':
    main()
