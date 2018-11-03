import sys, pygame, random

RED = (255, 0, 0)


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


width = 750
height = 750
screen = pygame.display.set_mode((width, height))
speed = [15, 15]
FPS = 30

square = pygame.image.load("square.png")
square = pygame.transform.scale(square, (110, 110))
square_rect = square.get_rect()
bkgd = pygame.image.load("background.png").convert()
bkgd_width = bkgd.get_rect().width
x = 0

class Square(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("square.png")
        self.rect = self.image.get_rect_rect()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key = pygame.key.get_pressed()
    all_sprites.update()

    if key[pygame.K_LEFT]:
        square_rect = square_rect.move([0, -7])
    if key[pygame.K_RIGHT]:
        square_rect = square_rect.move([0, 7])

    x -= 10
    if x == -bkgd_width:
        x = 0

    screen.blit(bkgd, (x, 0))
    screen.blit(bkgd, (x + bkgd_width, 0))
    all_sprites.draw(screen)
    screen.blit(square, square_rect)
    pygame.display.flip()
