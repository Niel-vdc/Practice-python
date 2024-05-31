import pygame
import pygame.draw
import pygame.time
import sys
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FRAME_RATE = 120

intensity = 5
total_drops = SCREEN_WIDTH * intensity

clock = pygame.time.Clock()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Droplet:
    x = 0
    y = 0
    width = 0
    height = 0
    colour = ()
    speed = 0
    gravity = 0
    z = 0
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(-SCREEN_HEIGHT, 0)
        self.z = random.randint(0, 20)
        self.width = random.randint(1, 2)
        self.height = random.randint(10, 20)
        self.colour = (150, 50, 150)
        self.speed = random.randint(2, 8)
        self.gravity = 0.03
        
    
    def drop(self):
        self.y += self.speed
        self.speed += self.gravity

        if self.y > SCREEN_HEIGHT:
            self.reset()
    
    def draw(self):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))

    def reset(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(-SCREEN_HEIGHT, 0)
        self.z = random.randint(0, 20)
        self.width = random.randint(1, 2)
        self.height = 15
        self.colour = (150, 50, 150)
        self.speed = random.randint(2, 10)
        self.gravity = 0.03
    

window.fill((255, 255, 255))
pygame.display.update()

droplets = []
for i in range(total_drops):
    droplet = Droplet()
    droplets.append(droplet)

while True:
    window.fill((200, 200, 200))

    for i in droplets:
        i.drop()
        i.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()
    clock.tick(FRAME_RATE)