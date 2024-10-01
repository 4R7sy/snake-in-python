# Inicial Configs
import pygame
import random

pygame.init()
pygame.display.set_caption("Snake")
width, height = 900, 600
display = pygame.display.set_mode((width, height))
oClock = pygame.time.Clock()  

# RGB Colors
black = (0, 0, 0)
green = (0, 255, 0)

# Snake Parameters
snakeHeight = 10
snakeSpeed = 15

def foodGenerator(pixels):
    while True:
        foodX = random.randint(0, (width - snakeHeight) // snakeHeight) * snakeHeight
        foodY = random.randint(0, (height - snakeHeight) // snakeHeight) * snakeHeight
        if (foodX, foodY) not in pixels:  
            return foodX, foodY

def drawFood(x, y):
    pygame.draw.rect(display, green, [x, y, snakeHeight, snakeHeight])  

def drawPoints(points):
    font = pygame.font.SysFont("Helvetica", 40)
    text = font.render("Your Points: {}".format(points), True, green)  
    display.blit(text, [1, 1])

def speedSelect(keys):
    speedX, speedY = 0, 0  
    if keys == pygame.K_DOWN:
        speedX, speedY = 0, 1
    if keys == pygame.K_UP:
        speedX, speedY = 0, -1
    if keys == pygame.K_LEFT:
        speedX, speedY = -1, 0
    if keys == pygame.K_RIGHT:
        speedX, speedY = 1, 0
    return speedX, speedY

def playGame():
    gameOver = False

    x = width // 2
    y = height // 2

    speedX = 0
    speedY = 0

    snakeLength = 1  
    pixels = []

    foodX, foodY = foodGenerator(pixels)  

    while not gameOver:
        display.fill(black)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            elif event.type == pygame.KEYDOWN:
                speedX, speedY = speedSelect(event.key)

        drawFood(foodX, foodY)  

        def drawSnake(height, pixels):
            for pixel in pixels:  
                pygame.draw.rect(display, green, [pixel[0], pixel[1], height, height])
        
       
        x += speedX * snakeHeight
        y += speedY * snakeHeight

       
        if x == foodX and y == foodY:  
            snakeLength += 1  
            foodX, foodY = foodGenerator(pixels)  

        
        pixels.append((x, y))  
        if len(pixels) > snakeLength:  
            del pixels[0]

       
        if x < 0 or x >= width or y < 0 or y >= height:  
            gameOver = True  

       
        for pixel in pixels[:-1]:
            if pixel == (x, y): 
                gameOver = True  

        drawSnake(snakeHeight, pixels)
        drawPoints(snakeLength - 1)  

        pygame.display.update()
        oClock.tick(snakeSpeed)

playGame()
