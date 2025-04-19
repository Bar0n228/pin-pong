from typing import Any
from pygame import *

class Game(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, hight):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Bone(Game):
    def update(self, speed):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= speed
        if key_pressed[K_DOWN] and self.rect.y < 460:
            self.rect.y += speed
    def left_update(self, speed):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= speed
        if key_pressed[K_s] and self.rect.y < 460:
            self.rect.y += speed

x_speed = 3
y_speed = 3
class Ball(Game):
    def update(self, x_speed, y_speed):
        self.rect.x += x_speed
        self.rect.y += y_speed
        if self.rect.y < 0:
            y_speed *= -1
        if self.rect.x > 1200 or self.rect.x <= 80:
            x_speed *= -1
        '''if sprite.spritecollide(bone_right, ball , False):
            x_speed *= -1'''

window = display.set_mode((1100, 700))
display.set_caption('Пин-понг')
background = transform.scale(image.load('background.jpg'),(1100, 700))

bone_right = Bone('bone.png', 1000, 200, 5, 50, 240)
bone_left = Bone('bone.png', 60, 200, 5, 50, 240)

ball = Ball('ball.png', 550, 1, 5, 70, 70)

font.init()
font1 = font.SysFont('Arial', 100)
font2 = font.SysFont('Arial', 50)

player_1 = 0
player_2 = 0
finish = False
game = True
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        bone_right.reset()
        bone_right.update(5)

        bone_left.reset()
        bone_left.left_update(5)

        lost_text = font1.render('GAME OVER', 1 , (255, 255, 255))
        count_text = font2.render(str(player_1) + ':' + str(player_2), 1, (255, 255, 255))
        window.blit(count_text, (500, 5))
        player1_text = font1.render('PLAYER 1 GETS 1 SCORE', 1, (255, 255, 255))
        player2_text = font1.render('PLAYER 2 GETS 1 SCORE', 1, (255, 255, 255))

        ball.reset()
        ball.rect.x += x_speed
        ball.rect.y += y_speed
        if ball.rect.y <=  0:
            y_speed *= -1
        if ball.rect.y >= 620:
            y_speed *= -1
        if ball.rect.colliderect(bone_right.rect) or ball.rect.colliderect(bone_left.rect):
            x_speed *= -1
        if ball.rect.x >= 1050:
            player_1 += 1
            window.blit(count_text, (500, 5))
            window.blit(player2_text, (450, 300))
            ball.rect.x = 550
            ball.rect.y = 1
            x_speed = 3
            y_speed = 3
        if ball.rect.x <= 50:
            player_2 += 1
            window.blit(count_text, (500, 5))
            window.blit(player1_text, (450, 300))
            ball.rect.x = 550
            ball.rect.y = 1
            x_speed = 3
            y_speed = 3


    display.update()
    clock.tick(FPS)
