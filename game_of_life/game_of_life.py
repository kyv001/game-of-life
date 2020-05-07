import pygame
from pygame.locals import *
from random import randint
from copy import copy

width = height = 80
screen_w = screen_h = 800
block_size_w = int(screen_w / width)
block_size_h = int(screen_h / height)

cells = [[int(randint(0,100) < 50) for __ in range(width)] for _ in range(height)]

pygame.init()
screen = pygame.display.set_mode((screen_w,screen_h))

def main(screen, cells):
    done = False
    while not done:
        cursor = [0, 0]
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True

        tmp_cells = [[cells[i][j] for j in range(len(cells[i]))] for i in range(len(cells))]
        while not cursor == [len(cells) - 1, len(cells[0]) - 1]:
            n_cells_around = 0
            '''
             _________________
            |-1 -1|0  -1|+1 -1|
            |-----|-----|-----|
            |-1  0|0   0|+1  0|
            |-----|-----|-----|
            |-1 +1|0  +1|+1 +1|
             ----------------- 
            '''
            try:
                if cells[cursor[0] - 1][cursor[1] - 1]:
                    n_cells_around += 1
            except IndexError:...
            try:
                if cells[cursor[0]][cursor[1] - 1]:
                    n_cells_around += 1
            except IndexError:...
            try:
                if cells[cursor[0] + 1][cursor[1] - 1]:
                    n_cells_around += 1
            except IndexError:...
            try:
                if cells[cursor[0] - 1][cursor[1]]:
                    n_cells_around += 1
            except IndexError:...
            try:
                if cells[cursor[0] + 1][cursor[1]]:
                    n_cells_around += 1
            except IndexError:...
            try:
                if cells[cursor[0] - 1][cursor[1] + 1]:
                    n_cells_around += 1
            except IndexError:...
            try:
                if cells[cursor[0]][cursor[1] + 1]:
                    n_cells_around += 1
            except IndexError:...
            try:
                if cells[cursor[0] + 1][cursor[1] + 1]:
                    n_cells_around += 1
            except IndexError:...

            if n_cells_around == 3:
                tmp_cells[cursor[0]][cursor[1]] = 1
            elif n_cells_around == 2:
                pass
            else:
                tmp_cells[cursor[0]][cursor[1]] = 0

            cursor[0] += 1
            if cursor[0] == len(cells[0]):
                cursor[0] = 0
                cursor[1] += 1

        cells = copy(tmp_cells)

        x, y = 0, 0
        for col in cells:
            for cell in col:
                pygame.draw.rect(screen,
                                 0xFFFFFF if cell else 0x000000,
                                 pygame.Rect((x * block_size_w,
                                              y * block_size_h),
                                             (block_size_w,
                                              block_size_h)))
                x += 1
            x = 0
            y += 1

        pygame.display.update()

if __name__ == '__main__':
    main(screen, cells)

