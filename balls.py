from pygame import *
from random import choice
p1_score = 0
p2_score = 0
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
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
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
#player1 = Player("player.png", 10, -10, 10, 16, 1000)     
#player2 = Player("player.png", 675, -10, 10, 16, 1000)
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size, size1):
        super().__init__(player_image, player_x, player_y, player_speed, size, size1)
        self.list_speed = [-6, -5, -4, -3, -2, 2, 3, 4, 5, 6]
        self.speed_x = choice(self.list_speed)
        self.speed_y = choice(self.list_speed)
        self.k = 0
    def update(self):
        self.reset()
        self.k += 0.0001
        if self.rect.y <= 0 or self.rect.y >= height - self.size1:
            self.speed_y *= -1
        if self.rect.x <= 0 or self.rect.x >= width - self.size:
            self.speed_x *= -1
        #if self.rect.colliderect(player1) or self.rect.colliderect(player2):
            #self.speed_x *= -1
        if self.speed_x > 0:
            self.speed_x += self.k
        elif self.speed_x < 0:
            self.speed_x -= self.k
        self.rect.x += self.speed_x + self.k
        self.rect.y += self.speed_y + self.k
ball = Ball("ball.png", 325, 230, 10, 50, 50)
ball1 = Ball("ball.png", 325, 230, 10, 50, 50)
ball2 = Ball("ball.png", 325, 230, 10, 50, 50)
ball3 = Ball("ball.png", 325, 230, 10, 50, 50)
ball4 = Ball("ball.png", 325, 230, 10, 50, 50)
ball5 = Ball("ball.png", 325, 230, 10, 50, 50)
ball6 = Ball("ball.png", 325, 230, 10, 50, 50)
ball7 = Ball("ball.png", 325, 230, 10, 50, 50)
ball8 = Ball("ball.png", 325, 230, 10, 50, 50)
ball9 = Ball("ball.png", 325, 230, 10, 50, 50)
clock = time.Clock()
FPS = 60
window = display.set_mode((700, 500))
display.set_caption("Пинг-понг")
background = transform.scale(image.load("background.png"), (width, height))
game = True
font.init()
font = font.SysFont("Arial", 25)
p1 = font.render(str(p1_score), False, (0, 0, 0))
p2 = font.render(str(p2_score), False, (0, 0, 0))
while game:
    window.blit(background, (0, 0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    p1.blit(window, (340, 30))
    p2.blit(window, (360, 30))
    #player1.reset()
    #player1.update()
    #player2.reset()
    #player2.update1()
    ball.update()
    ball1.update()
    ball2.update()
    ball3.update()
    ball4.update()
    ball5.update()
    ball6.update()
    ball7.update()
    ball8.update()
    ball9.update()
    clock.tick(FPS)    
    display.update()
