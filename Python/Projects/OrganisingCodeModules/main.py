from CellPackage.cells import *
from time import sleep

grid_size = 20
grid = create_live_grid(grid_size)
live_cells = []

def add_live_cells_to_list():   
    for cell in grid:
        if 1 in cell:
            live_cells.append((cell.index(1), grid.index(cell)))

def user_inupt_cell():
    x = input("Enter starting x: ")
    while not validate_input(x, grid_size):
        x = input("Enter starting x: ")

    y = input("Enter starting y: ")
    while not validate_input(y, grid_size):
        y = input("Enter starting y: ")

    cell = (int(x), int(y))
    edit_cell(cell, grid)

while True:
    add_live_cells_to_list()
    print_grid(grid, grid_size)

    for live_cell in live_cells:
        if len(list(get_live_neighbours(live_cell, grid))) < 2:
            edit_cell(live_cell, grid, 0)
        elif len(list(get_live_neighbours(live_cell, grid))) == 2 or len(list(get_live_neighbours(live_cell, grid))) == 3:
            edit_cell(live_cell, grid, 1)
        elif len(list(get_live_neighbours(live_cell, grid))) > 3:
            edit_cell(live_cell, grid, 0)

    for cell in get_dead_neighbours(live_cell, grid):
        if len(list(get_live_neighbours(cell, grid))) == 3:
            edit_cell(cell, grid, 1)