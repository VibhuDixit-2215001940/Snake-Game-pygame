import pygame
import random

#INITIALIZATION
pygame.init()

#VARIABLE INITIALIZATION
screen_width = 600
screen_height = 600
white = (255,255,255)
snake_x = 45
snake_y = 55
black = (0,0,0)
yellow = (255, 0, 0)
red = (255, 255, 0)
snake_size_x = 10
snake_size_y = 10
snake_size = 10
flag = False
game_over = False
fps = 30
velocity_x = 0
velocity_y = 0
food_x = random.randint(20,screen_width-50)
food_y = random.randint(20,screen_height-50)  
food_size = 5
score = 0
snk_list = []
snk_length = 1

# BACKGROUND SETTINGS
BACKGROUND_IMAGE = pygame.image.load("back.png")
background = pygame.transform.scale(BACKGROUND_IMAGE, (screen_width, screen_height))
BACKGROUND_X, BACKGROUND_Y = 0, 0

#MAKING SCREEN
canvas = pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)

#TITLE
pygame.display.set_caption("Snake Game")
pygame.display.update()

#ICON
icon = pygame.image.load("pic.png")
pygame.display.set_icon(icon)

#SNAKE LENGTH
def plot_snake(canvas, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(canvas, color, [x, y, snake_size, snake_size])

#SCORE BOARD
font = pygame.font.SysFont(None, 55)
def score_board(text, color,x ,y):
    screen_text = font.render(text, True, color)
    canvas.blit(screen_text, [x,y])

#GAME LOOP
clock = pygame.time.Clock()
while not flag:
    canvas.blit(background, (BACKGROUND_X, BACKGROUND_Y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 5
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = - 5
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = - 5
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                velocity_y = 5
                velocity_x = 0
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y
    if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
        score +=1
        snake_size_x += 10
        food_x = random.randint(20,screen_width-50)
        food_y = random.randint(20,screen_height-50) 
    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list)>snk_length:
        del snk_list[0]
    plot_snake(canvas, black, snk_list, snake_size)

    score_board("Score: "+str(score),red,5,5)
    pygame.draw.rect(canvas, black, [snake_x, snake_y, snake_size_x, snake_size_y])
    pygame.draw.circle(canvas, yellow, [food_x, food_y],radius=food_size)
    pygame.display.update()
    clock.tick(fps)