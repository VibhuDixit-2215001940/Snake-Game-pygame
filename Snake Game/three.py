import pygame
import random
import os

# INITIALIZATION
pygame.init()
pygame.mixer.init()

# Load background music
pygame.mixer.music.load('GameBackMusic.mp3')
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

# VARIABLE INITIALIZATION
screen_width = 600
screen_height = 600
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
snake_x = 45
snake_y = 55
snake_size = 10
flag = False
game_over = False
fps = 30
velocity_x = 0
velocity_y = 0
food_x = random.randint(20, screen_width - 50)
food_y = random.randint(20, screen_height - 50)
food_size = 5
score = 0
snk_list = []
snk_length = 1

# HIGHSCORE
with open("highscore.txt", "r") as f:
    highscore = int(f.read())

# GAME OVER ONLY
font = pygame.font.SysFont(None, 55)

def score_board(text, color, x, y):
    screen_text = font.render(text, True, color)
    canvas.blit(screen_text, [x, y])

# BACKGROUND SETTINGS
BACKGROUND_IMAGE = pygame.image.load("back.png")
background = pygame.transform.scale(BACKGROUND_IMAGE, (screen_width, screen_height))
BACKGROUND_X, BACKGROUND_Y = 0, 0

# SCORE PIC SETTINGS
SCORE_BACK = pygame.image.load("scorePic.jpeg")
backgroundScore = pygame.transform.scale(SCORE_BACK, (screen_width, screen_height))
BACKGROUND_x, BACKGROUND_y = 600, 600

# MAKING SCREEN
canvas = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

# TITLE
pygame.display.set_caption("Snake Game")
pygame.display.update()

# ICON
icon = pygame.image.load("pic.png")
pygame.display.set_icon(icon)

# SNAKE LENGTH
def plot_snake(canvas, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(canvas, color, [x, y, snake_size, snake_size])

# GAME LOOP
clock = pygame.time.Clock()
while not flag:
    if game_over:
        canvas.fill(white)
        canvas.blit(SCORE_BACK, (BACKGROUND_x, BACKGROUND_y))
        score_board("Game Over! Score: " + str(score), yellow, 100, 250)
        score_board("HighScore: " + str(highscore), red, 100, 300)
        score_board("Press Enter to continue...", red, 100, 350)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = True
    else:
        canvas.blit(background, (BACKGROUND_X, BACKGROUND_Y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = 5
                    velocity_y = 0
                if event.key == pygame.K_LEFT:
                    velocity_x = -5
                    velocity_y = 0
                if event.key == pygame.K_UP:
                    velocity_y = -5
                    velocity_x = 0
                if event.key == pygame.K_DOWN:
                    velocity_y = 5
                    velocity_x = 0
        snake_x = snake_x + velocity_x
        snake_y = snake_y + velocity_y
        if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
            # pygame.mixer.music.load('Eat.mp3')
            # pygame.mixer.music.play()
            score += 1
            snk_length += 1  # Increase snake length
            food_x = random.randint(20, screen_width - 50)
            food_y = random.randint(20, screen_height - 50)
            if score > int(highscore):
                highscore = score
        
        head = []
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)

        if len(snk_list) > snk_length:
            del snk_list[0]
        plot_snake(canvas, black, snk_list, snake_size)

        if head in snk_list[:-3]:
            game_over = True
            pygame.mixer.music.load('gameOver.mp3')
            pygame.mixer.music.play()
        if snake_x < 0 or snake_y < 0 or snake_x > screen_width or snake_y > screen_height:
            game_over = True
            pygame.mixer.music.load('gameOver.mp3')
            pygame.mixer.music.play()
            # print("GAME OVER ")
        score_board("Score: " + str(score), yellow, 5, 5)
        pygame.draw.rect(canvas, black, [snake_x, snake_y, snake_size, snake_size])
        pygame.draw.circle(canvas, red, [food_x, food_y], radius=food_size)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
