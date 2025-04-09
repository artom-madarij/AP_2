def valid(x, y, M, N, matrix, visited):
    if x < 0 or x >= M:
        return False
    if y < 0 or y >= N:
        return False
    if matrix[x][y] != 1:
        return False
    if visited[x][y]:
        return False
    return True


def distance(matrix, M, N):
    visited = []
    for i in range(M):
        visited.append([False] * N)
    queue = []
    for i in range(M):
        if matrix[i][0] == 1:
            queue.append((i, 0, 1))
            visited[i][0] = True
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        x, y, dist = queue.pop(0)
        if y == N - 1:
            return dist
        for dx, dy in direction:
            new_x, new_y = x + dx, y + dy
            if valid(new_x, new_y, M, N, matrix, visited):
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, dist + 1))
    return 0


def _file(filename):
    with open(filename, 'r') as file:
        matrix = []
        for lin in file:
            row = list(map(int, lin.split()))
            matrix.append(row)
    return matrix


filename = 'matrix.txt'
matrix = _file(filename)

M = len(matrix)
N = len(matrix[0])

result = distance(matrix, M, N)

if result != 0:
    print(f"довжина: {result}")
else:
    print("не існує шляху")
