from pygame import *
from random import randint

class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, player_speed, sixe_x, sixe_y):
        
        super().__init__()

        self.image = transform.scale(image.load(player_image), (sixe_x, sixe_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite): #класс для  игрока
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.x > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.x < win_width - 80:
           self.rect.y += self.speed
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.x > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.x < win_width - 80:
           self.rect.x += self.speed

         
    
win_width = 1000 #ширина экрана
win_height = 770 #высота экрана

window = display.set_mode((win_width, win_height)) #создание игрового окна
display.set_caption('ping pong') #название для окна
background = transform.scale(image.load("bg_bounty.jpg), (win_width, win_height)) #подгон заднего фона под размеры экрана
window.blit(background, (0, 0)) #фон на экран

gameOn = True
gameOver = False
clock = time.Clock()
FPS = 60

player_l = Player('b1.png', 5, 500, 10, 70, 170) #спрайт игрока1
player_l = Player('b2.png', 995, 500, 10, 70, 170) #спрайт игрока1
ball = GameSprite('kokos.png') #спрацт кокоса

speed_x = 3
speed_y = 3

#игровой цикл
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
            
    if gameOver != True:

        window.blit(background, (0, 0))
   
        player.update_l() #обновление игрока в игре
        player.reset()
        player.update_r() #обновление игрока в игре
        player.reset()
        

    display.update()
    clock.tick(FPS)
