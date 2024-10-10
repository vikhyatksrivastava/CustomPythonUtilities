from typing import List


def count_cross(grid: List[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    if rows < 3 or cols < 3:
        return 0

    # Precompute horizontal and vertical counts of consecutive 'X'
    horizontal_counts = [[0] * cols for _ in range(rows)]
    vertical_counts = [[0] * cols for _ in range(rows)]

    # Fill horizontal counts
    for i in range(rows):
        count = 0
        for j in range(cols):
            if grid[i][j] == 'X':
                count += 1
            else:
                count = 0
            horizontal_counts[i][j] = count

    # Fill vertical counts
    for j in range(cols):
        count = 0
        for i in range(rows):
            if grid[i][j] == 'X':
                count += 1
            else:
                count = 0
            vertical_counts[i][j] = count

    count = 0
    # Check for plus shapes
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if (grid[i][j] == 'X' and
                    horizontal_counts[i][j - 1] >= 1 and
                    horizontal_counts[i][j + 1] >= 1 and
                    vertical_counts[i - 1][j] >= 1 and
                    vertical_counts[i + 1][j] >= 1):
                count += 1

    return count


# Example test cases
print(count_cross(["......", "..XX..", ".XXXX.", "..XX..", "......"]))  # Should return 1
print(count_cross([".X.", "XXX", ".X."]))  # Should return 1
print(count_cross(["XXXX", "XXXX", "XXXX", "XXXX"]))  # Should return multiple pluses depending on the structure
print(count_cross([".", ".", "X", ".", "."]))  # Should return 0
print(count_cross(["X"]))  # Should return 0
