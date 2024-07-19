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
snake_size_x = 10
snake_size_y = 10
flag = False
game_over = False
fps = 30
velocity_x = 0
velocity_y = 0
food_x = random.randint(20,screen_width-50)
food_y = random.randint(20,screen_height-50)  
food_size = 5
score = 0

#MAKING SCREEN
canvas = pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)

#TITLE
pygame.display.set_caption("Snake Game")
pygame.display.update()

#ICON
icon = pygame.image.load("pic.png")
pygame.display.set_icon(icon)

#GAME LOOP
clock = pygame.time.Clock()
while not flag:
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
    if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<20:
        score +=1
        snake_size_x += 10
        print("Score: ",score)
        food_x = random.randint(20,screen_width-50)
        food_y = random.randint(20,screen_height-50) 
    canvas.fill(white)
    pygame.draw.rect(canvas, black, [snake_x, snake_y, snake_size_x, snake_size_y])
    pygame.draw.circle(canvas, yellow, [food_x, food_y],radius=food_size)
    pygame.display.update()
    clock.tick(fps)