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
        draw.rect(window,BACKGROUND,self.rect)
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        draw.rect(window,BACKGROUND,self.rect)
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_l(self):
        draw.rect(window,BACKGROUND,self.rect)
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

racket_r = Player("racket.png",30,80,win_width - 40,200,3)
racket_l = Player("racket.png",30,80,10,200,3)
ball = GameSprite("tenis_ball.png",50,50,325,225,0)

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        racket_r.update_r()
        racket_l.update_l()

        racket_r.reset()
        racket_l.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)