import pytest

from entity.constants import CELL_MAX, GRID_SIZE, MAGIC_SUM


@pytest.fixture
def grid_g1():
    """G1 — 부분 격자, 0이 2개 at (2,2)·(3,3) 1-index, row-major."""
    grid = [
        [16, 3, 2, 13],
        [5, 0, 11, 8],
        [9, 6, 0, 12],
        [4, 15, 14, 1],
    ]
    assert len(grid) == GRID_SIZE
    assert all(len(row) == GRID_SIZE for row in grid)
    assert sum(cell == 0 for row in grid for cell in row) == 2
    assert MAGIC_SUM == 34  # fixture anchor — SSOT from entity.constants
    assert CELL_MAX == 16
    return grid
