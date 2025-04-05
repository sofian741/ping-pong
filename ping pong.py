from pygame import *

win_width ,win_height = 700,500
BACKGROUND = (200 ,255 ,255)
window = display.set_mode((win_width,win_height))
window.fill(BACKGROUND)
display.set_caption("Ping Pong")
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, filename, width, height, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(filename),(width , height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):

        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_l(self):
        
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

racket_r = Player("racket.png",30,80,win_width - 40,200,3)
racket_l = Player("racket.png",30,80,10,200,3)
ball = GameSprite("tenis_ball.png",50,50,325,225,0)

font.init()
font_1 = font.SysFont("Arial",65,True)
win_r = font_1.render("Right Player WON",True,(180,0,0))
win_l = font_1.render("Left Player WON",True,(180,0,0))

speed_x = 3
speed_y = 3

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        window.fill(BACKGROUND)
        racket_r.update_r()
        racket_l.update_l()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 450 or ball.rect.y <0:
            speed_y *= -1

        if sprite.collide_rect(ball , racket_r) or sprite.collide_rect(ball,racket_l):
            speed_x *= -1

        if ball.rect.x > 650:
            window.blit(win_l,(125,225))
            finish = True

        if ball.rect.x < 0:
            window.blit(win_r,(125,225))
            finish = True

        racket_r.reset()
        racket_l.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)