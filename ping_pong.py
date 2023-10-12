from pygame import *


#Создай собственный Шутер!
from random import *

# привет ))))
# как дела? 

r = 700
r2 = 500
window = display.set_mode((r, r2))
display.set_caption("Ping_pong")

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width = 45, height = 70, player_speed_y = 0):
        super().__init__()
        
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed_y = player_speed_y
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
goal1 = 0
goal2 = 0
class Enemy(GameSprite):
    
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed_y
        if self.rect.y <= 0 or self.rect.y >= r2:
            self.speed_y *= -1
        
        if self.rect.x >= r:
            global goal1
            goal1 += 1
            self.rect.x = 250
            self.rect.y = 200

        if self.rect.x <= 0:
            global goal2
            goal2 += 1
            self.rect.x = 250
            self.rect.y = 200



        # self.rect.y += self.speed
        # if self.rect.y >= 500:
        #     global lost
        #     lost += 1
        #     self.rect.y = -10
        #     self.rect.x = randint(10,690)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
    

sprite1 = Player("pr.png", 620, 200, 3) 
sprite2 = Player2("pr.png",0, 200, 3) 
# sprite2 = Enemy("rocket.png", 500, 50, 1)
ball = Enemy("b.png", 200, 200, 1 , 65, 65, -1)

print('hello')
 
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


goal_text1 = font1.render('Игрок1', True, (100, 250, 100))
goal_text2 = font2.render('Игрок2',True,(250,100,100))
# loser = font1.render('Пропущено: '+ str(lost), True, (250, 100, 100)) 
play = True
# sprite2.set_direction()
while game:
    if play:
        window.fill((255, 187, 153))
        sprite1.reset()
        sprite1.update()
        
        sprite2.update()
        sprite2.reset()

        ball.reset()
        ball.update()
        bullets.draw(window)
        bullets.update()
        # if ball.rect.y == 0:
        if sprite.collide_rect(ball, sprite1) or sprite.collide_rect(ball, sprite2):
            ball.speed *= -1


        # window.blit(win,(10,0))
        
        goal_text1 = font1.render('Игрок1: '+ str(goal1),  True, (100, 250, 100))
        window.blit(goal_text1,(10,30))
        goal_text2 = font1.render('Игрок2: '+ str(goal2),  True, (100, 250, 100))
        window.blit(goal_text2,(500,30))
        # if lost >= 10 or sprite.spritecollide(sprite1, enemies, True):
        #     text = font2.render('Проигрыш',True,(250,100,100))
        #     window.blit(text,(200,250))
        #     play = False
   

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    
