import pygame
from settings import *
from snake import Snake
from food import Food
from ui import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game PRO - AZMATH")

clock = pygame.time.Clock()


# 🔥 High Score Functions
def load_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except:
        return 0

def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))


def game():
    snake = Snake()
    food = Food()
    score = 0
    high_score = load_high_score()

    paused = False
    running = True

    while running:
        gradient_bg(screen, WIDTH, HEIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif event.key == pygame.K_DOWN and snake.direction != "UP":
                    snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                    snake.direction = "RIGHT"
                elif event.key == pygame.K_p:
                    paused = not paused

        # ⏸️ Pause logic
        if paused:
            draw_text(screen, "PAUSED ⏸️", 50, HEIGHT//2)
            pygame.display.update()
            continue

        snake.move()

        # 🍎 Eat food
        if snake.body[0] == food.position:
            snake.grow = True
            food.position = food.spawn()
            score += 10

            # 💾 Update high score
            if score > high_score:
                high_score = score
                save_high_score(high_score)

        # 💀 Collision
        if snake.check_collision(WIDTH, HEIGHT):
            game_over_screen(screen, WIDTH, HEIGHT, score)
            return

        snake.draw(screen)
        food.draw(screen)

        # 🎯 Updated score UI
        draw_score(screen, score, high_score)

        pygame.display.update()
        clock.tick(FPS)


# 🎮 Start screen
start_screen(screen, WIDTH, HEIGHT)

# 🔁 Game loop
while True:
    game()