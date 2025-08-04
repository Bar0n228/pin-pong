from typing import Any
from pygame import *
from time import sleep

class Game(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, hight):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.visible = True
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Bone(Game):
    def update(self, speed):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= speed
        if key_pressed[K_DOWN] and self.rect.y < 550:
            self.rect.y += speed
    def left_update(self, speed):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= speed
        if key_pressed[K_s] and self.rect.y < 500:
            self.rect.y += speed

a = 5
x_speed = a
y_speed = a
class Ball(Game):
    def update(self):
        if self.visible:
            self.reset()



window = display.set_mode((1300, 900))
display.set_caption('Пин-понг')
background = transform.scale(image.load('wallpapers.jpeg'),(1300, 900))

bone_right = Bone('blue_weapon.png', 1150, 200, 5, 40, 350)
bone_left = Bone('red_weapon.png', 60, 200, 5, 40, 350)

ball = Ball('ball.png', 550, 1, 5, 90, 90)


font.init()
font1 = font.SysFont('Arial', 100)
font2 = font.SysFont('Arial', 80)

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
        window.blit(count_text, (600, 5))
        player1_text = font1.render('PLAYER 1 GETS 1 SCORE', 1, (255, 255, 255))
        player2_text = font1.render('PLAYER 2 GETS 1 SCORE', 1, (255, 255, 255))

        player1_win = font1.render('PLAYER 1 WIN!', 1, (255, 255, 255))
        player2_win = font1.render('PLAYER 2 WIN!', 1, (255, 255, 255))

        if player_1 == 5:
            window.blit(player1_win, (380, 300))
            finish = True

        if player_2 == 5:
            window.blit(player2_win, (380, 300))
            finish = True
    
        ball.update()
        ball.rect.x += x_speed
        ball.rect.y += y_speed

        if ball.rect.y <=  0:
            y_speed *= -1

        if ball.rect.y >= 810:
            y_speed *= -1

        if ball.rect.colliderect(bone_right.rect) or ball.rect.colliderect(bone_left.rect):
            x_speed *= -1

        if ball.rect.x >= 1300:
            player_1 += 1
            window.blit(count_text, (600, 5))
            window.blit(player1_text, (200, 300))
            display.flip()  
            time.wait(1500)
            ball.rect.x = 550
            ball.rect.y = 1
            x_speed = a
            y_speed = a

        if ball.rect.x <= -90:
            player_2 += 1
            window.blit(count_text, (600, 5))
            window.blit(player2_text, (200, 300))
            display.flip()  
            time.wait(1500)
            ball.rect.x = 550
            ball.rect.y = 1
            x_speed = a
            y_speed = a
        

    display.update()
    clock.tick(FPS)
