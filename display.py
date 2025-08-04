import pygame

# Function to display the score
def display_score(score, font):
    value = font.render("Your Score: " + str(score), True, (255, 255, 255))
    pygame.display.get_surface().blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_List, screen):
    for x in snake_List:
        pygame.draw.rect(screen, (0, 5, 7), [x[0], x[1], snake_block, snake_block])

# Function to display messages
def show_message(msg, color):
    font_style = pygame.font.SysFont("bahnschrift", 25)
    mesg = font_style.render(msg, True, color)
    screen = pygame.display.get_surface()
    screen.blit(mesg, [screen.get_width() / 6, screen.get_height() / 3])
    
    
