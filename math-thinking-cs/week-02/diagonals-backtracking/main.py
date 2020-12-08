import sys


def is_full(g, n):
    for i in range(n):
        if -1 in g[i]:
            return False
    return True


def is_valid(g, n, c, r):
    if g[r][c] == 0:
        return True
    if r - 1 >= 0:
        if g[r - 1][c] != 0 and g[r - 1][c] != g[r][c]:
            return False
    if (r + 1) % n > 0 and c - 1 >= 0:
        if g[r + 1][c - 1] == 2 and g[r][c] == 2:
            return False
    if c - 1 >= 0:
        if g[r][c - 1] != 0 and g[r][c - 1] != g[r][c]:
            return False
    if r - 1 >= 0 and c - 1 >= 0:
        if g[r - 1][c - 1] == 1 and g[r][c] == 1:
            return False
    return True


def get_next(n, r, c):
    if r + 1 > n - 1:
        return (r + 1) % n, c + 1
    else:
        return r + 1, c


def solve(g, n, r, c, q):
    if is_full(g, n):
        count = 0
        for i in range(n):
            for j in range(n):
                if g[j][i] != 0:
                    count += 1
        if count == q:
            for i in range(n):
                print(*g[i])
            exit(0)
        return
    for k in [1, 2, 0]:
        g[c][r] = k
        if is_valid(g, n, r, c):
            _next = get_next(n, r, c)
            solve(g, n, _next[0], _next[1], q)
        g[c][r] = -1


if __name__ == '__main__':
    nx = int(5)
    goal = int(16)
    grid = []
    for _ in range(nx):
        grid.append([-1] * nx)
    solve(grid, nx, 0, 0, goal)
