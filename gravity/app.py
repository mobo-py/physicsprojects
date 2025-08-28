import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

mode = 'setting'
bg = None  # background image
selected_planet = None  # store clicked planet name


class Planet:
    def __init__(self, name, x, y, image_path):
        self.name = name
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))  # clickable area

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


# Define planets
mercury = Planet('mercury', 20, 100, 'gravity/planets/icon/mercury.png')
venus   = Planet('venus', 120, 100, 'gravity/planets/icon/venus.png')
earth   = Planet('earth', 220, 100, 'gravity/planets/icon/earth.png')
mars    = Planet('mars', 320, 100, 'gravity/planets/icon/mars.png')
jupiter = Planet('jupiter', 420, 100, 'gravity/planets/icon/jupiter.png')
saturn  = Planet('saturn', 520, 100, 'gravity/planets/icon/saturn.png')
uranus  = Planet('uranus', 620, 100, 'gravity/planets/icon/uranus.png')
neptune = Planet('neptune', 720, 100, 'gravity/planets/icon/neptune.png')

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

mercurygravity = 3.7
venusgravity = 8.87
earthgravity = 9.81
marsgravity = 3.71
jupitergravity = 24.79
saturngravity = 10.44
uranusgravity = 8.69
neptunegravity = 11.15

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vy = 0  # vertical velocity
        self.radius = 15

    def update(self, gravity):
        self.vy += gravity * 0.1  # simulate gravity effect
        self.y += self.vy

        # Bounce off the ground
        if self.y + self.radius > 600:
            self.y = 600 - self.radius
            self.vy = -self.vy * 0.7  # lose some energy on bounce

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (int(self.x), int(self.y)), self.radius)
    def reset(self, x, y):
        self.x = x
        self.y = y
        self.vy = 0
ball = Ball(400, 50)
while running:
    # ---- handle events ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            mode = 'setting'
            bg = None
            selected_planet = None
            ball.reset(400, 50)

        if mode == 'setting' and event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            for p in planets:
                if p.rect.collidepoint(mx, my):
                    selected_planet = p.name
                    print("Selected:", selected_planet)
                    # load background once and scale it to screen
                    bg = pygame.image.load(f'gravity/planets/surface/{selected_planet}.jpg')
                    bg = pygame.transform.scale(bg, (800, 600))
                    mode = 'running'

    # ---- drawing ----
    if mode == 'setting':
        screen.fill((0, 0, 0))
        for p in planets:
            p.draw(screen)

        font = pygame.font.Font(None, 36)
        tip = font.render("Press on any planet to start", True, (255, 255, 255))
        screen.blit(tip, (400 - tip.get_width() // 2, 400))

    elif mode == 'running':
        if bg:
            screen.blit(bg, (0, 0))
        
        match selected_planet:
            case 'mercury':
                gravity = mercurygravity
            case 'venus':
                gravity = venusgravity
            case 'earth':
                gravity = earthgravity
            case 'mars':
                gravity = marsgravity
            case 'jupiter':
                gravity = jupitergravity
            case 'saturn':
                gravity = saturngravity
            case 'uranus':
                gravity = uranusgravity
            case 'neptune':
                gravity = neptunegravity
        
        ball.update(gravity)
        ball.draw(screen)
        

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
