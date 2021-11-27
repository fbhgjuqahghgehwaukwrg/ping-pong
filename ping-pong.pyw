from pygame import *
from random import choice
direction = "up"
direction1 = "left"
list_speed = [-8, -7, -6, -5, 5, 6, 7, 8]
ball_speed_x = choice(list_speed)
ball_speed_y = choice(list_speed)
width = 700
height = 500
ball_size = 30
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
clock = time.Clock()
FPS = 60
window = display.set_mode((700, 500))
display.set_caption("Пинг-понг")
background = transform.scale(image.load("background.png"), (width, height))
game = True
player1 = Player("player.png", 10, 176, 10, 16, 148)
player2 = Player("player.png", 675, 176, 10, 16, 148)
ball = GameSprite("ball.png", 325, 230, 10, 40, 40)
font.init()
font = font.SysFont("Arial", 25)
while game:
    window.blit(background, (0, 0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    if ball.rect.y <= 0 or ball.rect.y >= height - ball.size1:
        ball_speed_y *= -1
    if ball.rect.colliderect(player1) or ball.rect.colliderect(player2):
        ball_speed_x *= -1
    ball.rect.x += ball_speed_x
    ball.rect.y += ball_speed_y
    player1.reset()
    player1.update()
    player2.reset()
    player2.update1()
    ball.reset()
    ball.update
    clock.tick(FPS)    
    display.update()
