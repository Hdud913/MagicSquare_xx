from entity.constants import BLANK_CELL, GRID_SIZE, INDEX_ORIGIN


def find_blank_coords(grid):
    """Return 1-index (row, col) for each blank cell, row-major order."""
    coords = []
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == BLANK_CELL:
                coords.append((row + INDEX_ORIGIN, col + INDEX_ORIGIN))
    return coords
