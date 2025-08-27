import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
mode = 'setting'






black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)

screencolor = (0, 0, 0)


rightforce = 0
leftforce = 0
upforce = 0
downforce = 0

class object:
    def __init__(self, x, y, l, color, rightforce, leftforce, upforce, downforce):
        self.x = x
        self.y = y
        self.l = l
        self.color = color
    def update(self):
        self.x += rightforce
        self.x -= leftforce
        self.y += downforce
        self.y -= upforce    
    
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x-self.l, self.y-self.l, self.l*2, self.l*2))

object = object(400, 300, 100, white, rightforce, leftforce, upforce, downforce)
xrange = range(object.x-object.l, object.x + object.l)
yrange = range(object.y-object.l, object.y + object.l)
while running:
    screen.fill(black)
    mousepos = pygame.mouse.get_pos()
    if mode == 'setting':
        object.draw()
        
        



        mode = 'running'

    else:
        object.update()
        object.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    
