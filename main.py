import configparser
from logging import config
import os
import random
import time

config = configparser.ConfigParser()  # noqa: F811
config.read("settings.ini")

ROWS = config.getint("game", "rows")
COLS = config.getint("game", "columns")
DEAD = 0
ALIVE = 1

def create_random_grid(rows, cols):
    return [[random.randint(DEAD, ALIVE) for _ in range(cols)] for _ in range(rows)]

def create_empty_grid(rows, cols):
    return [[DEAD for _ in range(cols)] for _ in range(rows)]

def print_grid(grid, generation=None):
    if generation is not None:
        print(f"Generation: {generation}")
    print("-" * len(grid[0]))
    for rows in grid:
        print("".join("O" if cell else " " for cell in rows))
    print("-" * len(grid[0]))

def amount_of_neighbors(grid, row: int, col: int):
    amount = 0
    for r in (-1, 0, 1):
        for c in (-1, 0, 1):
            if r == c == 0:
                continue
            target_row = row + r
            target_col = col + c
            if 0 <= target_row < len(grid) and 0 <= target_col < len(grid[0]):
                amount += grid[target_row][target_col]
    return amount

def next_generation(grid):
    rows = len(grid)
    cols = len(grid[0])
    next_grid = create_empty_grid(rows, cols)
    for row in range(rows):
        for col in range(cols):
            neighbors = amount_of_neighbors(grid, row, col)
            if grid[row][col] and (neighbors == 2 or neighbors == 3):
                next_grid[row][col] = ALIVE
            if (not grid[row][col]) and neighbors == 3:
                next_grid[row][col] = ALIVE
    return next_grid

GENERATIONS = config.getint("game", "generations")
GENERATION_DELAY = config.getfloat("game", "generation_delay")
grid = create_random_grid(ROWS, COLS)
for i in range(GENERATIONS):
    time.sleep(GENERATION_DELAY)
    os.system("cls" if os.name == "nt" else "clear")
    print_grid(grid, generation=i)
    grid = next_generation(grid)
