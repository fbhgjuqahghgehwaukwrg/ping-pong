from pygame import *
from random import choice
from PIL import Image
import os
width = 700
height = 500
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size, size1):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size, size1))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
        self.size = size
        self.size1 = size1
        self.image_name = player_image
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size, size1):
        super().__init__(player_image, player_x, player_y, player_speed, size, size1)
        self.score = 0
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s]:
            if self.rect.y < 352:
                self.rect.y += self.speed
            else:
                self.rect.y = 352
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed
        if keys[K_DOWN]:
            if self.rect.y < 352:
                self.rect.y += self.speed
            else:
                self.rect.y = 352
player1 = Player("player.png", 10, 176, 10, 16, 148)     
player2 = Player("player.png", 675, 176, 10, 16, 148)
font.init()
font = font.SysFont("Arial", 25)
p1 = font.render(str(player1.score), True, (0, 0, 0))
p2 = font.render(str(player2.score), True, (0, 0, 0))
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size, size1):
        super().__init__(player_image, player_x, player_y, player_speed, size, size1)
        self.list_speed = [-6, -5, -4, -3, -2, 2, 3, 4, 5, 6]
        self.speed_x = choice(self.list_speed)
        self.speed_y = choice(self.list_speed)
        self.k = 0
    def update(self):
        global p1, p2
        self.reset()
        self.k += 0.0001
        if self.rect.y <= 0 or self.rect.y >= height - self.size1:
            self.speed_y *= -1
        if self.rect.x <= -5:
            self.rect.x = width / 2 - self.size / 2
            self.rect.y = height / 2 - self.size1 / 2
            self.speed_x = choice(self.list_speed)
            self.speed_y = choice(self.list_speed)
            player2.score += 1
            time.delay(200)
            window.blit(background, (0, 0))
            p1 = font.render(str(player1.score), True, (0, 0, 0))
            p2 = font.render(str(player2.score), True, (0, 0, 0))
            window.blit(p1, (305, 30))
            window.blit(p2, (390, 30))
            player1.reset()
            player1.update()
            player2.reset()
            player2.update1()
            self.reset()
            clock.tick(FPS)    
            display.update()
            time.delay(1000)
        elif self.rect.x >= width - self.size + 5:
            self.rect.x = width / 2 - self.size / 2
            self.rect.y = height / 2 - self.size1 / 2
            self.speed_x = choice(self.list_speed)
            self.speed_y = choice(self.list_speed)
            player1.score += 1
            time.delay(200)
            window.blit(background, (0, 0))
            p1 = font.render(str(player1.score), True, (0, 0, 0))
            p2 = font.render(str(player2.score), True, (0, 0, 0))
            window.blit(p1, (305, 30))
            window.blit(p2, (390, 30))
            player1.reset()
            player1.update()
            player2.reset()
            player2.update1()
            self.reset()
            clock.tick(FPS)    
            display.update()
            time.delay(1000)
        if self.rect.colliderect(player1) or self.rect.colliderect(player2):
            self.speed_x *= -1
        if self.speed_x > 0:
            self.speed_x += self.k
        elif self.speed_x < 0:
            self.speed_x -= self.k
        self.rect.x += self.speed_x + self.k
        self.rect.y += self.speed_y + self.k
ball = Ball("ball.png", 325, 230, 10, 40, 40)
clock = time.Clock()
FPS = 60
window = display.set_mode((700, 500))
display.set_caption("Пинг-понг")
background = transform.scale(image.load("background.png"), (width, height))
game = True
finish = False
while game:
    window.blit(background, (0, 0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    if player1.score == 5:
        finish = "Первый игрок выиграл"
    elif player2.score == 5:
        finish = "Второй игрок выиграл"
    if not finish:
        window.blit(p1, (305, 30))
        window.blit(p2, (390, 30))
        player1.reset()
        player1.update()
        player2.reset()
        player2.update1()
        ball.update()
        clock.tick(FPS)    
        display.update()
    else:
        if finish == "Первый игрок выиграл":
            p1_x = player1.rect.x
            while True:
                for i in event.get():
                    if i.type == QUIT:
                        exit()
                window.blit(background, (0, 0))
                if p1_x != player1.rect.x + 150:
                    p1_x += 1
                if player1.rect.y != height / 2 - player1.size1 / 2:
                    if player1.rect.y > height / 2 - player1.size1 / 2:
                        player1.rect.y -= 1
                    elif player1.rect.y < height / 2 - player1.size1 / 2:
                        player1.rect.y += 1
                window.blit(player1.image, (p1_x, player1.rect.y))
                win = font.render(finish, True, (0, 0, 0))
                window.blit(win, (410, 235))
                display.update()
        elif finish == "Второй игрок выиграл":
            p2_x = player2.rect.x
            while True:
                for i in event.get():
                    if i.type == QUIT:
                        exit()
                window.blit(background, (0, 0))
                if p2_x != player2.rect.x - 150:
                    p2_x -= 1
                if player1.rect.y != height / 2 - player1.size1 / 2:
                    if player1.rect.y > height / 2 - player1.size1 / 2:
                        player1.rect.y -= 1
                    elif player1.rect.y < height / 2 - player1.size1 / 2:
                        player1.rect.y += 1
                window.blit(player2.image, (p2_x, player1.rect.y))
                win = font.render(finish, True, (0, 0, 0))
                window.blit(win, (75, 235))
                display.update()



