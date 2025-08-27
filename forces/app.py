import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
mode = 'setting'

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)
blue = (50, 120, 255)

# Forces
rightforce = 0
leftforce = 0
upforce = 0
downforce = 0

# Slider class
class Slider:
    def __init__(self, x, y, w, name, value=0, max_val=10):
        self.x = x
        self.y = y
        self.w = w
        self.h = 6
        self.knob_r = 10
        self.name = name
        self.max_val = max_val
        self.knob_x = self.x + (value / max_val) * self.w
        self.dragging = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] - self.knob_x) ** 2 + (event.pos[1] - self.y) ** 2 <= self.knob_r ** 2:
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False

    def update(self):
        if self.dragging:
            mx = pygame.mouse.get_pos()[0]
            self.knob_x = max(self.x, min(mx, self.x + self.w))

    def get_value(self):
        return (self.knob_x - self.x) / self.w * self.max_val

    def draw(self, surface):
        pygame.draw.rect(surface, gray, (self.x, self.y - self.h // 2, self.w, self.h))
        pygame.draw.circle(surface, blue, (int(self.knob_x), self.y), self.knob_r)
        font = pygame.font.Font(None, 26)
        text = font.render(f"{self.name}: {self.get_value():.1f}", True, white)
        surface.blit(text, (self.x + self.w + 20, self.y - 10))

# Object class
class GameObject:
    def __init__(self, x, y, l, color):
        self.x = x
        self.y = y
        self.l = l
        self.color = color

    def update(self, rf, lf, uf, df):
        self.x += rf
        self.x -= lf
        self.y -= uf
        self.y += df

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x - self.l, self.y - self.l, self.l * 2, self.l * 2))

# Create object
obj = GameObject(400, 300, 50, white)

# Create sliders
sliders = [
    Slider(20, 100, 200, "Right", 0),
    Slider(20, 160, 200, "Left", 0),
    Slider(20, 220, 200, "Up", 0),
    Slider(20, 280, 200, "Down", 0),
]

while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for s in sliders:
            s.handle_event(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # SPACE toggles mode
                mode = "running" if mode == "setting" else "setting"

    if mode == "setting":
        obj.rightforce = 0
        obj.leftforce = 0
        obj.upforce = 0
        obj.downforce = 0

        obj.x = 400
        obj.y = 300
        obj.draw(screen)
        for s in sliders:
            s.update()
            s.draw(screen)

        font = pygame.font.Font(None, 36)
        tip = font.render("Press SPACE to start", True, white)
        screen.blit(tip, (400-120, 400))

    else:  # running mode
        rightforce = sliders[0].get_value()
        leftforce = sliders[1].get_value()
        upforce = sliders[2].get_value()
        downforce = sliders[3].get_value()

        obj.update(rightforce, leftforce, upforce, downforce)
        obj.draw(screen)

        font = pygame.font.Font(None, 36)
        tip = font.render("Press SPACE to adjust forces", True, white)
        screen.blit(tip, (100, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
