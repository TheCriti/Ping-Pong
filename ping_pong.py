from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        pressed = key.get_pressed()
        if pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if pressed[K_s] and self.rect.y < w - 80:
            self.rect.y += self.speed
    def update2(self):
        pressed = key.get_pressed()
        if pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if pressed[K_DOWN] and self.rect.y < w - 80:
            self.rect.y += self.speed
            
class Enemy(GameSprite):
    def update(self):
        self.speed = 2
        self.rect.y = 0
        self.rect.x = 200
w = 516
h = 516
speed = 3

rocket1 = Player('rocket.png', 0, 0, 5, 100, 100)
rocket2 = Player('rocket.png', 408, 5, 5, 100, 100)
ball = Enemy('ball.png', 129, -10, 3, 40, 40)

window = display.set_mode((516, 516))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('background.png'), (w, h))
game = True
finish = False

font.init()
font1 = font.SysFont('Arial', 36)
clock = time.Clock()
FPS = 60

win = font1.render('ТЫ ВЫИГРАЛ!!!', True, (255, 255, 255))
lose = font1.render('ТЫ ПРОИГРАЛ!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0))
        rocket1.update1()
        rocket2.update2()
        ball.update()
        rocket1.reset()
        rocket2.reset()
        ball.rect.y += ball.speed
        ball.rect.x += ball.speed
        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            ball.speed *= -1
        ball.reset()
        display.update()
    clock.tick(FPS)
