import random

# Function to generate food
def generate_food(width, height, snake_block):
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    return foodx, foody
