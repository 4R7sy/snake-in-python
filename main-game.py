# Inicial Configs
import pygame
import random

pygame.init()
pygame.display.set_caption("Snake")
width, height = 900, 600
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock

# RGB Colors
black = (0, 0, 0)
green = (0, 255, 0)

# Smake Parameters
snakeHeight = 10
snakeSpeed = 15

def foodGenerator():
    foodX = random.randint(0, 900)
    foodY = random.randint(0, 600)
    return foodX, foodY

def playGame():
    gameOver = False

    x = width / 2
    y = height / 2

    speedX = 0
    speedY = 0

    snake = 1
    pixels = []

    foodX, foodY = foodGenerator()



    while not gameOver:
        display.fill(black)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
# Infinite Loop

# Draw the Game Objects

# Creating the Logic

playGame()