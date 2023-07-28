def num_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(row, col):
        if (row, col) in visited:
            return
        visited.add((row, col))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                dfs(r, c)

    island_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                island_count += 1
                dfs(r, c) # recursion which uses stack to store functions in LIFO order

    return island_count

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(num_islands(grid)) 