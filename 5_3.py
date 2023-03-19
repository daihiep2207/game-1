from pygame import *

# The Setup class uses init method to automatically load, scale and identify the rectangle of  an object. The class has the reset method to use when we need to make the character appear on the window.
class Setup():
    def __init__(self, imagename, width, height, x,y):
        self.imagename = transform.scale(image.load(imagename), (width,height))
        self.rect = self.imagename.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self): 
        w.blit(self.imagename,(self.rect.x,self.rect.y))

#The class Player with the class Setup inside its parentheses, which mean the Player inherit, take all the information and method from the Setup.
class Player(Setup):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x-=20
        if keys[K_RIGHT]:
            self.rect.x+=20
        if keys[K_UP]:
            self.rect.y-=20
        if keys[K_DOWN]:
            self.rect.y+=20 

#Class Wall contains 4 parameters which is automatically used for the identifying the size and the coordinate of a object that we wanna Draw into the screen.
#But this object is not an image inserted from a file on our computer, it is written and drawn directly in the program, so that's why it's separated frome the class Setup and we  don't use the class Setup for identifying this object, we create the class Wall for drawing it.
#We cannot create an rectangle outside this object because it's not an image as we did with above objects, this one is a thing that we draw directly inside the program, so we need to find out a way to create a rectangle for this objects.
#The variable self.image was use as a surface,this surface will be used as an image with the same size, coordinate of this object, and because it's an image, we can create the rectangle for it.
class Wall():
    def __init__(self, x,y,width, height):
        self.x = x
        self.y = y  
        self.width = width
        self.height = height
        self.image = Surface([self.width, self.height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect = Rect(self.x, self.y, self.width, self.height)
    def wallrect(self):
        draw.rect(w, (0,0,0), (self.x, self.y, self.width, self.height)) 
class Bomb(Setup):
    side = "left"
    def bombmovement(self):
        if self.rect.x>640:
            self.side = "left"
        if self.rect.x<430:
            self.side = "right"
        if self.side == "right":
            self.rect.x += 5
        else:
            self.rect.x -= 5

#Display the window
w = display.set_mode((700,700))
display.set_caption("5/3")

#setup the size for each character with proper class
player = Player("player.png", 80,100, 50,600)
background = Setup("forest.png", 100,100, 600, 600)
bomb = Bomb("bom.png", 60,60, 600, 500)
wall = Wall(400,250,30,450)
horizontalwall = Wall(200,220,350,30)


time1 = True
time2 = True



while time1:

    if time2:
        w.fill((255,255,255))
        wall.wallrect()
        horizontalwall.wallrect()
        player.update()
        player.reset()
        
        background.reset()
        bomb.bombmovement()
        bomb.reset()
        if sprite.collide_rect(background, player):
            winimage = image.load("winning.jpg")
            winimage = transform.scale(winimage, (300,300))
            w.blit(winimage,(200,200))
            time2 = False
        if sprite.collide_rect(bomb, player):
            w.blit(transform.scale(image.load("losing.webp"),(300,300)),(200,200))
            time2 = False
        if sprite.collide_rect(wall, player) or sprite.collide_rect(horizontalwall, player):
            w.blit(transform.scale(image.load("losing.webp"),(300,300)),(200,200))
            time2 = False
    for e in event.get():
        if e.type == QUIT:
            time1 = False
        if e.type == KEYDOWN:
            if e.key == K_e:
                player = Player("player.png", 80,100, 50,600)
                background = Setup("forest.png", 100,100, 600, 600)
                bomb = Bomb("bom.png", 60,60, 600, 500)
                wall = Wall(400,250,30,450)
                horizontalwall = Wall(200,220,350,30)
                time2 = True
    display.update()
    time.delay(50)
