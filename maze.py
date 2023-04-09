#создай игру "Лабиринт"!
from pygame import *
mixer.init()
#создай окно игры

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.diraction = 'left'

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 625:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 425:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, player_speed)
        self.diraction = 'left'
    def update(self):
        if self.rect.x <= 420:
            self.diraction = 'right'
        if self.rect.x >= 700 - 70:
            self.diraction = 'left'
        if self.diraction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed 

class Wall(sprite.Sprite):
    def __init__(self, color, wallX, wallY, width, height):
        sprite.Sprite.__init__(self)
        self.color = color
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = wallX
        self.rect.y = wallY
    def drawWall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



window = display.set_mode((700, 500))
display.set_caption("Лабиринт")

player = Player("source\\hero.png", 5, 250, 4)
enemy = Enemy("source\\cyborg.png", 500, 250, 1)
treasure = GameSprite('source\\treasure.png', 625, 30, 0)

background = transform.scale(image.load("source\\background.jpg"), (700, 500))
#player = transform.scale(image.load("source\\hero.png"), (75, 75))
#enemy = transform.scale(image.load("source\\cyborg.png"), (75, 75))

clock = time.Clock()
FPS = 60

#mixer.music.load('source\\jungles.ogg')
#mixer.music.play()
#money = mixer.Sound("source\\money.ogg")
#kick = mixer.Sound("source\\kick.ogg")

w1 = Wall((154, 205, 50), 100, 20 , 500, 10)
w2 = Wall((154, 205, 50), 100, 480, 600, 10)
w3 = Wall((154, 205, 50), 100, 20 , 10, 380)
w4 = Wall((154, 205, 50), 200, 100 , 10, 380)
w5 = Wall((154, 205, 50), 300, 20 , 10, 380)
w6 = Wall((154, 205, 50), 400, 100 , 10, 380)
w7 = Wall((154, 205, 50), 500, 100 , 10, 380)
w8 = Wall((154, 205, 50), 600, 20 , 10, 380)

game = True
finish = False
while game:
    for n in event.get():
        if n.type == QUIT:
            game = False

    if not finish:
        window.blit(background,(0, 0))
        enemy.update()
        player.update()
        

        player.reset()
        enemy.reset()
        treasure.reset()

        w1.drawWall()
        w2.drawWall()
        w3.drawWall()
        w4.drawWall()
        w5.drawWall()
        w6.drawWall()
        w7.drawWall()
        w8.drawWall()

        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
            finish = True
            window.blit(lose, (200, 200))
            #kick.play()

        if sprite.collide_rect(player, treasure):
            finish = True
            window.blit(win, (200, 200))
            #money.play()

        display.update()
        clock.tick(60)