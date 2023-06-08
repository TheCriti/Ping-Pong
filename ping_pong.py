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
        self.rect.y = ball_y
        self.rect.x = ball_x
w = 516
h = 516
speed_x = 2
speed_y = 2
ball_y = 0
ball_x = 200

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

win1 = font1.render('ЛЕВЫЙ ИГРОК ВЫИГРАЛ!!!', True, (180, 0, 0))
lose1 = font1.render('ПРАВЫЙ ИГРОК ВЫИГРАЛ!!!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    rocket1.update1()
    rocket2.update2()
    ball.update()
    rocket1.reset()
    rocket2.reset()
    ball.reset()
    if not finish:
        ball_x += speed_x
        ball_y += speed_y
        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball_y == 486 or ball_y == 0:
            speed_y *= -1
        if ball_x < 0:
            finish = True
            window.blit(lose1, (75, 222))
        if ball_x > 516:
            finish = True
            window.blit(win1, (75, 222))
        display.update()
    clock.tick(FPS)
