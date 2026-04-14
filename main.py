import random
import time

ROWS = 20
COLS = 40

def create_random_grid(rows, cols):
    return [[random.randint(0,1) for _ in range(cols)] for _ in range(rows)]

def create_empty_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    for rows in grid:
        print("".join("O" if cell else " " for cell in rows))

def get_amount_of_neighbors(grid, row: int, col: int):
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

def get_next_generation(grid):
    rows = len(grid)
    cols = len(grid[0])
    next_grid = create_empty_grid(rows, cols)
    for row in range(rows):
        for col in range(cols):
            neighbors = get_amount_of_neighbors(grid, row, col)
            if grid[row][col] and (neighbors == 2 or neighbors == 3):
                next_grid[row][col] = 1
            if (not grid[row][col]) and neighbors == 3:
                next_grid[row][col] = 1
    return next_grid

GENERATIONS = 100
grid = create_random_grid(ROWS, COLS)
for i in range(GENERATIONS):
    time.sleep(0.1)
    print(f"Generation: {i}")
    print_grid(grid)
    grid = get_next_generation(grid)
