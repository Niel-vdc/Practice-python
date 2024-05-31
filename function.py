import pygame
import pygame.draw
import math
 
# Define some colors
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# initialise pygame
pygame.init()
 
# Set the width and height of the screen [width, height]
WIDTH = 700
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
clock = pygame.time.Clock()

step = 1 # amount of pixels per x value

coordinates = []

origin = (WIDTH/2, HEIGHT/2)

for i in range(math.floor(WIDTH/step)):
    x = i * step - origin[0]
    function = ( 30 * pow(x + 30, 3) + 100 * pow(x, 2) + 100 *x) * 0.001
    y = HEIGHT - function - origin[1]
    coordinates.append((i*step, y))
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(WHITE)

    pygame.draw.line(screen, GRAY, (origin[0], HEIGHT), (origin[0], 0))
    pygame.draw.line(screen, GRAY, (0, origin[1]), (WIDTH, origin[1]))
    pygame.draw.lines(screen, BLACK, False, coordinates)
    
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()