from pygame import *
from random import randint

class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, player_speed, sixe_x = 65, sixe_y = 65):
        
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
win_height = 769 #высота экрана

window = display.set_mode((win_width, win_height)) #создание игрового окна
display.set_caption('ping pong') #название для окна
background = transform.scale(image.load("bg.jpg"), (win_width, win_height)) #подгон заднего фона под размеры экрана
window.blit(background, (0, 0)) #фон на экран

game_on = True
game_over = False
clock = time.Clock()
FPS = 60

player_l = Player('p1.png', ) #спрайт игрока1
player_l = Player('p2.png', ) #спрайт игрока1


#игровой цикл
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
            
    if finish == False:

        window.blit(background, (0, 0))
   
        player.update_l() #обновление игрока в игре
        player.reset()
        player.update_r() #обновление игрока в игре
        player.reset()


        text_lose = font1.render(
        "Пропущено: " + str(lost), 1, (0, 0, 0)
        )
        window.blit(text_lose, (0, 20))

        text_score = font1.render(
        "Счет: " + str(score), 1, (0, 0, 0)
        )
        window.blit(text_score, (0, 60))

    else:
        if key.get_pressed()[K_r]:
            finish = False
            score = 0
            lost = 0

    display.update()
    clock.tick(FPS)
