from pygame import *


#Создай собственный Шутер!

from pygame import *
from random import *

# привет ))))
# как дела? 

r = 700
r2 = 500
window = display.set_mode((r, r2))
display.set_caption("Ping_pong")

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width = 65, height = 65):
        super().__init__()
        
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < (r2 - 105):
            self.rect.y += self.speed
        if keys_pressed[K_SPACE]:
            bullet = Bullet('bullet.png', self.rect.centerx - 4 , self.rect.y, 5, 15, 10)
            bullets.add(bullet)

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < (r2 - 105):
            self.rect.y += self.speed
        if keys_pressed[K_SPACE]:
            bullet = Bullet('bullet.png', self.rect.centerx - 4 , self.rect.y, 5, 15, 10)
            bullets.add(bullet)
lost = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            global lost
            lost += 1
            self.rect.y = -10
            self.rect.x = randint(10,690)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
    

sprite1 = Player("pr.png", 400, 430, 3) 
sprite2 = Player2("pr.png", 200, 430, 3) 
# sprite2 = Enemy("rocket.png", 500, 50, 1)
ball = Enemy("b.png", 50, -10, 2)


 
game = True
mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
# kick = mixer.Sound('fire.ogg')
# kick.play()


font.init()
font1 = font.SysFont('Arial', 35)
font2 = font.SysFont('Arial', 90)

bullets = sprite.Group()


win = font1.render('Счет:', True, (100, 250, 100))
text = font2.render('Проигрыш',True,(250,100,100))
# loser = font1.render('Пропущено: '+ str(lost), True, (250, 100, 100)) 
play = True
# sprite2.set_direction()
while game:
    if play:
        window.fill((255, 187, 153))
        sprite1.update()
        sprite1.reset()
        sprite2.update()
        sprite2.reset()

        ball.reset()
        ball.update()
        bullets.draw(window)
        bullets.update()

        window.blit(win,(10,0))
        
        loser = font1.render('Пропущено: '+ str(lost), True, (250, 100, 100)) 
        window.blit(loser,(10,30))
        # if lost >= 10 or sprite.spritecollide(sprite1, enemies, True):
        #     text = font2.render('Проигрыш',True,(250,100,100))
        #     window.blit(text,(200,250))
        #     play = False
   

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    
