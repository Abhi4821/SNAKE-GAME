import pygame
import time
#import random
from settings import WIDTH, HEIGHT,  SNAKE_SPEED,SNAKE_BLOCK
from display import display_score, draw_snake, show_message 
from food import generate_food

# Initialize Pygame
pygame.init()

# Display settings
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game : Made By :  Abhishek Yadav || Vivek Yadav || Sushant Singh || Narayn')

# Font settings
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Main function for the game
def gameLoop():
    
    cl=pygame.mixer.Sound("MP3.mp3")
    pygame.mixer.Sound.play(cl)
    
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx, foody = generate_food(WIDTH, HEIGHT, SNAKE_BLOCK)

    clock = pygame.time.Clock()
    i=1
    while not game_over:
        
        while game_close:
            SCREEN.fill((250,190,203))# Pink background  
            show_message("Game End              Start New Game Enter : C           Close Window Enter:Q", (213, 50, 80))
            display_score(Length_of_snake - 1, score_font)
            pygame.display.update()
            
            if i==1:
                sm=pygame.mixer.Sound("distory.wav")
                pygame.mixer.Sound.play(sm)
            i=i+1
            
            

            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                    
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True                                             #   129, 245, 105
        x1 += x1_change
        y1 += y1_change
        SCREEN.fill((102,73,2 ))  # Pink background
        pygame.draw.rect(SCREEN, (244,233,46), [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_List, SCREEN)
        display_score(Length_of_snake - 1, score_font)

        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food(WIDTH, HEIGHT, SNAKE_BLOCK)
            Length_of_snake += 1
            son=pygame.mixer.Sound("eat.wav")
            pygame.mixer.Sound.play(son)
            
            
        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


gameLoop()       