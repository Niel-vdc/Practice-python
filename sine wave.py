import pygame
import pygame.draw
import pygame.display
import pygame.mouse
import math
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


step = 1000

x = 0
y = 0

circle_x = x

enlarge = 50

points = []

i = 0
for i in range(round((math.pi*2 * step)) * 4):
    x = i / step
    y = math.sin(x)

    points.append([x, y])

    i += 1


while True:
    mouse = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    screen.fill((200, 200, 200))

    for i in range(len(points)):
        if i != len(points) - 1:
            pygame.draw.line(screen, (0, 0, 0), (points[i][0] * enlarge + 20, points[i][1] * enlarge + 200), (points[i+1][0] * enlarge + 20, points[i+1][1] * enlarge + 200), 4)
    
    pygame.draw.circle(screen, (200, 30, 80), (circle_x + 20, math.sin(circle_x/enlarge) * enlarge + 200), 20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    
    circle_x = mouse[0]
    
    pygame.display.update()
    clock.tick(60)