import pygame
import pygame.draw
import random
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

status = False

y = []
for i in range(SCREEN_HEIGHT):
    y.append(SCREEN_HEIGHT-i)

random.shuffle(y)

def draw():
    for i in range(len(y)):
        pygame.draw.line(screen, (0, 0, 0), (i, SCREEN_HEIGHT), (i, y[i]))

def sort():
    for i in range(len(y) - 1):
        if y[i] > y[i + 1]:
            y[i + 1], y[i] = y[i], y[i + 1]



def test() -> bool:
    counter = 0
    for i in range(len(y) - 1):
        if y[i] < y[i+1]:
            counter += 1
    
    if counter == len(y) - 1:
        return True
    else:
        return False

start_test = False

while True:
    screen.fill((200, 200, 200))
    
    draw()

    if start_test:
        while not test():
            sort()
            break
        if test():
            print("Done!")
            status = True
            start_test = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if status == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_test = True
        if status:
            if event.type == pygame.MOUSEBUTTONDOWN:
                random.shuffle(y)
                status = False
    
    pygame.display.update()
    clock.tick(60)