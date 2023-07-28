from collections import deque

def has_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = deque([start])

    while queue:
        row, col = queue.popleft()
        if (row, col) == end:
            return True
        print(visited)
        if (row, col) not in visited:
            visited.add((row, col))
            for dr, dc in [(0,1), (0,-1), (1, 0), (-1, 0)]:
                r, c = row + dr, col + dc

                while 0 <= r < rows and 0 <= c < cols and maze[r][c] ==0:
                    r, c = r + dr, c + dc

                r, c = r - dr, c - dc
                print((r,c))
                queue.append((r, c))

    return False


maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]

start = (0, 4)
destination = (4, 4)

print(has_path(maze, start, destination))