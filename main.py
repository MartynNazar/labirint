import pygame


class Player:
    def __init__(self,speed,width,height,x,y,skin):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width,height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def draw(self,window):
        window.blit(self.texture,self.hitbox)


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.hitbox.x += self.speed
        if keys[pygame.K_DOWN]:
            self.hitbox.y += self.speed
        if keys[pygame.K_LEFT]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_UP]:
            self.hitbox.y -= self.speed



class Wall:
    def __init__(self,width,height,x,y,color):
        self.hitbox = pygame.Rect(x,y,width,height)
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window,self.color,self.hitbox)



class Gold:
    def __init__(self,width,height,x,y,skin):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width,height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def draw(self,window):
        window.blit(self.texture,self.hitbox)





pygame.init()



window = pygame.display.set_mode([700,500])
fps = pygame.time.Clock()
player = Player(5,50,50,50,225,"hero.png")
gold = Gold(50,50,600,160,"treasure.png")
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, [700,500])
game = True

walls = [
    Wall(100,20,50,100,[123,123,123]),
    Wall(100,20,50,400,[123,123,123]),
    Wall(500,20,150,100,[123,123,123]),
    Wall(500,20,150,400,[123,123,123]),
    Wall(20,320,650,100,[123,123,123]),
    Wall(500,20,150,100,[123,123,123]),
    Wall(20, 100, 50, 100, [123, 123, 123]),
    Wall(20, 100, 50, 300, [123, 123, 123]),
    Wall(20, 100, 400, 100, [123, 123, 123]),
    Wall(250, 20, 150, 180, [123, 123, 123]),
    Wall(100, 20, 50, 300, [123, 123, 123]),
    Wall(20, 100, 300, 180, [123, 123, 123]),
    Wall(20, 100, 450, 300, [123, 123, 123]),
    Wall(105, 20, 450, 300, [123, 123, 123]),
    Wall(20, 120, 535, 200, [123, 123, 123]),
]


while game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            print(x,y)
    window.fill([255,0,0])
    window.blit(background,[0,0])
    player.draw(window)
    gold.draw(window)

    player.move()

    for wall in walls:
        if player.hitbox.colliderect(wall.hitbox):
            player.hitbox.x = 50
            player.hitbox.y = 225



    for wall in walls:
        wall.draw(window)
    pygame.display.flip()

    fps.tick((60))
