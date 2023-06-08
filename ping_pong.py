#Создай собственный Шутер!

from pygame import *
from random import *
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
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
        if self.rect.y <= 500:
            self.rect.y += self.speed
        else:
            self.rect.y = 0
            self.rect.x = randint(0, 650)
            self.speed = randint(1, 3)

w = 516
h = 516

rocket1 = Player('rocket.png', 5, 5, 5)
rocket2 = Player('rocket.png', 500, 5, 5)
ball = Enemy('ball.png', 129, -10, 3)

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
        display.update()
    clock.tick(FPS)