import pygame
from pygame.locals import *

cells = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

pygame.init()
screen = pygame.display.set_mode((160,160))

def main(screen):
    f_done = False
    while not f_done:
        cursor = [0, 0]
        for event in pygame.event.get():
            if event.type == QUIT:
                f_done = True

        while cursor == [len(cells) - 1, len(cells[0]) - 1]:
            n_cells_around = 0
            if cursor == [0, 0]:
                if cells[cursor[0] + 1][cursor[1]]:
                    n_cells_around += 1
                if cells[cursor[0]][cursor[1] + 1]:
                    n_cells_around += 1
                    
            elif cursor[0] == 0:
                if cells[cursor[0] + 1][cursor[1]]:
                    n_cells_around += 1
                if cells[cursor[0]][cursor[1] - 1]:
                    n_cells_around += 1
                if cells[cursor[0]][cursor[1] + 1]:
                    n_cells_around += 1
                    
            elif cursor[1] == 0:
                if cells[cursor[0] - 1][cursor[1]]:
                    n_cells_around += 1
                if cells[cursor[0] + 1][cursor[1]]:
                    n_cells_around += 1
                if cells[cursor[0]][cursor[1] + 1]:
                    n_cells_around += 1
                    
            else:
                if cells[cursor[0] - 1][cursor[1]]:
                    n_cells_around += 1
                if cells[cursor[0] + 1][cursor[1]]:
                    n_cells_around += 1
                if cells[cursor[0]][cursor[1] - 1]:
                    n_cells_around += 1
                if cells[cursor[0]][cursor[1] + 1]:
                    n_cells_around += 1

            if n_cells_around >= 3 and cells[cursor[0]][cursor[1]]:
                cells[cursor[0]][cursor[1]] = 0
            if n_cells_around == 2 and not cells[cursor[0]][cursor[1]]:
                cells[cursor[0]][cursor[1]] = 1

        pygame.display.update()
