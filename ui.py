import pygame

WHITE = (255,255,255)

# ✅ Gradient Background
def gradient_bg(screen, width, height):
    for y in range(height):
        color = (y % 255, (y*2) % 255, (y*3) % 255)
        pygame.draw.line(screen, color, (0, y), (width, y))


# ✅ Center Text
def draw_text(screen, text, size, y):
    font = pygame.font.SysFont("Segoe UI", size, bold=True)
    render = font.render(text, True, WHITE)
    rect = render.get_rect(center=(screen.get_width()//2, y))
    screen.blit(render, rect)


# ✅ Score Display
def draw_score(screen, score, high_score):
    font = pygame.font.SysFont("Segoe UI", 22, bold=True)

    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    screen.blit(font.render(f"High Score: {high_score}", True, (255,255,0)), (10, 40))
    screen.blit(font.render("P = Pause | Arrows = Move", True, (200,200,200)), (10, 70))


# ✅ Button Class
class Button:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, screen):
        pygame.draw.rect(screen, (50,150,255), self.rect, border_radius=10)
        font = pygame.font.SysFont("Segoe UI", 25, bold=True)
        txt = font.render(self.text, True, (255,255,255))
        screen.blit(txt, txt.get_rect(center=self.rect.center))

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.rect.collidepoint(event.pos)


# ✅ Start Screen
def start_screen(screen, width, height):
    start_btn = Button("START", width//2 - 75, height//2, 150, 50)

    while True:
        gradient_bg(screen, width, height)
        draw_text(screen, "🐍 SNAKE PRO", 60, height//3)

        start_btn.draw(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); quit()

            if start_btn.is_clicked(event):
                return


# ✅ Game Over Screen
def game_over_screen(screen, width, height, score):
    restart_btn = Button("RESTART", width//2 - 75, height//2 + 60, 150, 50)

    while True:
        gradient_bg(screen, width, height)

        draw_text(screen, "GAME OVER 💀", 60, height//3)
        draw_text(screen, f"Score: {score}", 30, height//2)

        restart_btn.draw(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); quit()

            if restart_btn.is_clicked(event):
                return