import random
import pygame
from pygame.constants import K_LSUPER, MOUSEWHEEL
import pygame.draw
import pygame.mouse
import pygame.key
import pygame.event
import sys
import math

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


class Box:
    def __init__(self, position_x, position_y, width, height, color = (255, 255, 255)) -> None:
        self.posx = position_x
        self.posy = position_y
        self.width = width
        self.height = height
        self.color = color

        self.tl = (position_x - width/2, position_y - height/2)
        self.tr = (position_x + width/2, position_y - height/2)
        self.bl = (position_x - width/2, position_y + height/2)
        self.br = (position_x + width/2, position_y + height/2)

        self.perspective = [0, 0]

    def draw(self):
        pygame.draw.polygon(screen, self.color, (self.tl, self.tr, self.br, self.bl))

    def update(self, events):
        self.tl = (self.posx - self.width/2, self.posy - self.height/2)
        self.tr = (self.posx + self.width/2, self.posy - self.height/2)
        self.bl = (self.posx - self.width/2, self.posy + self.height/2)
        self.br = (self.posx + self.width/2, self.posy + self.height/2)

        mouse = pygame.mouse.get_pressed()
        mouse_movement = pygame.mouse.get_rel()
        key = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.MOUSEWHEEL:
                if key[pygame.K_LSUPER or pygame.K_RSUPER]:
                    self.width += event.y
                    self.height += event.y
                    
            if mouse[0]:
                self.posx += mouse_movement[0]/2
                self.posy += mouse_movement[1]/2
                self.perspective[0] += mouse_movement[0]/500
                self.perspective[1] += mouse_movement[1]/500

                
                    

color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))


box = Box(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 200, 200, color)

while True:
    screen.fill((200, 200, 200))

    box.draw()

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
            
    box.update(events)
    pygame.display.update()
    clock.tick(60)