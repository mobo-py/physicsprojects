import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True


class Ball:
    def __init__(self, x, y, f, d):
        self.x = x
        self.y = y
        self.f = f
        self.d = d
        self.radius = 15

        if self.d == 'l':
            self.f = abs(self.f) * -1
        else:
            self.f = abs(self.f)

    def update(self):
        self.x += self.f

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (int(self.x), int(self.y)), self.radius)


ball1 = Ball(100, 300, 5, 'r')
ball2 = Ball(700, 300, 5, 'l')
balls = [ball1, ball2]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for ball in balls:
        ball.update()
        ball.draw(screen)

    # Check for collision
    if abs(ball1.x - ball2.x) <= ball1.radius + ball2.radius:
        ball1.f, ball2.f = ball2.f, ball1.f  # swap forces

    pygame.display.flip()
    clock.tick(60)