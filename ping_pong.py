#code game
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,w,h,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 615:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 615:
            self.rect.y += self.speed
background = transform.scale(image.load("Amerima.jpg"),(700,500))
win_height = 500
win_width = 700
window = display.set_mode((700,500))
racket1 = Player("mini.png",600,70,40,50,10)
racket2 = Player("mini.png",10,70,40,50,10)
ball = Player("ball.png",333,200,30,40,5)
speed_x = 3
speed_y = 3
font.init()
font1 = font.Font(None,35)
lose1 = font1.render('PLAYER 1 LOSEEE!', True, (180,0,0))
font2 = font.Font(None,35)
lose2 = font2.render('PLAYER 2 LOSEEE!', True, (180,0,0))
game = True
finish = False
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0,0))
        racket1.update_l()
        racket2.update_r()
        ball.reset()
        racket1.reset()
        racket2.reset()
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > win_height-50 or ball.rect.y < 50:
        speed_y *= -1
    if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
        speed_x *= -1
    if ball.rect.y < 0:
        finish = True
        window.blit(lose1,(200,200))
        game = False
    if ball.rect.x > win_width:
        finsih = True
        window.blit(lose2,(200,200))
        game = False
        

    display.update()
    clock.tick(60)
