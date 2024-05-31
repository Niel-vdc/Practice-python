import random
import sys

import pygame
import pygame.draw
import pygame.font
import pygame.mouse

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

shapes = []


class Shape():
    def __init__(self, color) -> None:
        self.points_list = []
        self.points_tuple = self.points_list
        self.started = 0
        self.color = color
        self.surface = screen
    
    def update(self):
        mouse = pygame.mouse.get_pressed()

        mouse_pos = pygame.mouse.get_pos()

        self.points_tuple = self.points_list

        if self.started == 1:
            self.points_list = [mouse_pos, mouse_pos, mouse_pos]

        if self.started > 1:
            pygame.draw.polygon(self.surface, self.color, self.points_tuple)

        if mouse[0]:
            self.started += 1
            new_point = pygame.mouse.get_pos()
            self.points_list.append(new_point)



random_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

shape = Shape(random_color)


while True:
    screen.fill((200, 200, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            shapes.append(shape)
            del shape
            random_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
            shape = Shape(random_color)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                shapes = []
            if event.key == pygame.K_BACKSPACE:
                shapes = shapes[:-1]
    
    
    for i in shapes:
        pygame.draw.polygon(i.surface, i.color, i.points_tuple)
    shape.update()
    pygame.display.update()
    clock.tick(60)