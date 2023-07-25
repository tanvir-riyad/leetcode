# find the perimeter of island where 1 is land, 0 is water

def island_perimeter(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 1

                
                if r < rows - 1 and grid[r + 1][c] == 1:
                    perimeter -= 1

                
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 1

              
                if c < cols - 1 and grid[r][c + 1] == 1:
                    perimeter -= 1

    return perimeter


grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid))  
