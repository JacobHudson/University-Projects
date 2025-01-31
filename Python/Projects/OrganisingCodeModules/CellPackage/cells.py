from itertools import product  
import tkinter as tk 

window = tk.Tk()
window.title("conway's game of life ish")
window.geometry("500x500") # Set the window size

def get_neighbours(cell, gridsize):
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell and all(0 <= n < gridsize for n in c):
            yield c

def get_live_neighbours(cell, grid):
    all_neighbours = get_neighbours(cell, len(grid))
    for cell in all_neighbours:
        if grid[cell[1]][cell[0]] == 1:
            yield cell

def get_dead_neighbours(cell, grid):
    all_neighbours = get_neighbours(cell, len(grid))
    for cell in all_neighbours:
        if grid[cell[1]][cell[0]] == 0:
            yield cell

def print_grid(grid, gridsize):
    for i in range(gridsize):
        for j in range(gridsize):
            # print(grid[i][j], end=' ')
            v = tk.Label(window, text= str(grid[i][j]))
            v.grid(row=i, column=j)
            window.update()

def create_dead_grid(gridsize):
    return [[0 for _ in range(gridsize)] for _ in range(gridsize)]

def create_live_grid(gridsize):
    return [[1 for _ in range(gridsize)] for _ in range(gridsize)]

def create_random_grid(gridsize):
    import random
    return [[random.choice([0, 1]) for _ in range(gridsize)] for _ in range(gridsize)]

def edit_cell(cell, grid, cell_value=1):
    grid[cell[1]][cell[0]] = cell_value

def validate_input(value, gridsize):
    if not value.isdigit():
        return False
    return 0 <= int(value) < gridsize