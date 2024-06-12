import numpy as np
import pygame
import time

# Colors used in program
color_bg=(25, 24, 30)
color_grid=(40,40,40)
color_die_next=(170,170,170)
color_alive_next=(255,255,255)

# Update Function
def update (screen, cells, size, with_progress=False): #updates the display
    update_cells = np.zeros(cells.shape, dtype=int) #display cells

    for row, col in np.ndindex(cells.shape): #iterate over all individual cells using row and columns
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row,col] #calculate alive cells from neighbour cells
        color = color_bg if cells[row, col]==0 else color_alive_next #determined the color

        # Rules of the game
        if cells[row, col]==1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color=color_die_next
            elif 2 <= alive <= 3:
                update_cells[row, col] =1
                if with_progress:
                    color= color_alive_next
        else:
            if alive == 3:
                update_cells[row,col] =1
                if with_progress:
                    color = color_alive_next

        pygame.draw.rect(screen, color, (col*size,row*size, size-1, size-1)) # made a rectangle
    return update_cells

def main():
    pygame.init()
    screen= pygame.display.set_mode((800,600))

    cells = np.zeros((60, 80), dtype=int) #initialised a playing field
    screen.fill(color_grid)  #the grid
    update(screen, cells,10)

    pygame.display.flip()
    pygame.display.update()

    running =  False

    # Taking user input from mouse and keyboard
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(color_grid)

        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()

        time.sleep(0.001)

if __name__=='__main__':
    main()



#
# Created by Ishant Singh on 12-06-2024
# Copyright (c) 2024 Ishant Singh. All rights reserved.
