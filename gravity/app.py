import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

mode = 'setting'


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

planet = None

while running:
    # ---- handle events ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if mode == 'setting' and event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            for p in planets:
                if p.rect.collidepoint(mx, my):
                    planet = p.name
                    print("Selected:", planet)
                    mode = 'running'

    # ---- drawing ----
    screen.fill((0, 0, 0))

    if mode == 'setting':
        # Draw planets
        for p in planets:
            p.draw(screen)

        font = pygame.font.Font(None, 36)
        tip = font.render("Press on any planet to start", True, (255, 255, 255))
        screen.blit(tip, (400 - tip.get_width() // 2, 400))

    else:  # running mode
        for i in planets:
            match i:
                case 'mercury':
                    bg = pygame.image.load(f'gravity/planets/surface/{i}.jpg')
                    screen.blit(bg, (0, 0))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
