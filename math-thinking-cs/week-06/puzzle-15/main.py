goal_pos = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]


def is_even_permutation(p):
    t = 0
    while True:
        done = True
        for i in range(len(p) - 1):
            if p[i] > p[i + 1]:
                done = False
                p[i], p[i + 1] = p[i + 1], p[i]
                t = t + 1
        if done:
            break
    return t % 2 == 0


def get_matrix(arr, n=4):
    return [arr[i:i + n] for i in range(0, len(arr), n)]


def get_target_goal_pos(matrix, moves_map, n=4):
    k = 0, 0
    for i in range(n - 1):
        for row in range(i, n):
            if matrix[row][i] == goal_pos[k[0]][k[1]]:
                moves_map[row][i] = 1
                if row + 1 < n:
                    k = row + 1, i
                else:
                    k = i, i + 1
            else:
                return k
        for col in range(i + 1, n):
            if matrix[i][col] == goal_pos[k[0]][k[1]]:
                moves_map[i][col] = 1
                if col + 1 < n:
                    k = i, col + 1
                else:
                    k = i + 1, i + 1
            else:
                return k
    return n - 1, n - 1


def get_actual_pos(target, matrix, n=4):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == target:
                return i, j
    return 0, 0


def explore_neighbours(moves_map, visited, qr, qc, prev, row, col):
    r_dir = [-1, 1, 0, 0]
    c_dir = [0, 0, -1, 1]
    for i in range(len(r_dir)):
        rr = row + r_dir[i]
        cc = col + c_dir[i]
        if rr < 0 or cc < 0 or rr > 3 or cc > 3 or visited[rr][cc]:
            continue
        if moves_map[rr][cc] in [1, 2]:
            continue
        qr.append(rr)
        qc.append(cc)
        visited[rr][cc] = True
        prev[rr][cc] = row, col


def bfs(moves_map, sr, sc):
    qr = []
    qc = []
    qr.append(sr)
    qc.append(sc)
    visited = [[False] * 4 for _ in range(4)]
    visited[sr][sc] = True
    prev = [[None] * 4 for _ in range(4)]
    while len(qr) > 0:
        row = qr.pop(0)
        col = qc.pop(0)
        explore_neighbours(moves_map, visited, qr, qc, prev, row, col)
    return prev


def reconstruct_path(prev, begin_row, begin_col):
    moves = []
    row = begin_row
    col = begin_col
    while prev[row][col] is not None:
        moves.append((row, col))
        row, col = prev[row][col]
    moves.reverse()
    return moves


def get_path(_from, _to, _grid):
    if _from[0] == _to[0] and _from[1] == _to[1]:
        return [_from]
    parents = bfs(_grid, _from[0], _from[1])
    return reconstruct_path(parents, _to[0], _to[1])


def swap(matrix, row, col, blank_pos, moves):
    if matrix[row][col] != 0:
        moves.append(matrix[row][col])
    matrix[row][col], matrix[blank_pos[0]][blank_pos[1]] = \
        matrix[blank_pos[0]][blank_pos[1]], matrix[row][col]
    return row, col


def move_along_path(p, blank_pos, target_pos, matrix, moves, moves_map):
    for row, col in p:
        blank_pos = swap(matrix, row, col, blank_pos, moves)
    swap(matrix, target_pos[0], target_pos[1],
         blank_pos, moves)
    moves_map[target_pos[0]][target_pos[1]] = 0


def flip(matrix, blank_pos, times, first_step, clockwise, moves):
    rd = [0, -1, 0, 1]
    cd = [-1, 0, 1, 0]
    i = first_step
    count = 0
    tmp = blank_pos
    while count < times:
        tmp = swap(matrix, tmp[0] + rd[i], tmp[1] + cd[i], tmp, moves)
        if clockwise:
            i = (i + 1) % 4
        else:
            i = (i - 1) % 4
        count = count + 1
    return tmp


def resolve_collision(matrix, blank_pos, t_row, t_col, moves):
    tmp = blank_pos
    if t_row == 3:
        if blank_pos[0] > t_col:
            tmp = flip(matrix, blank_pos, 1, 0, True, moves)
        else:
            tmp = flip(matrix, blank_pos, 3, 2, True, moves)
        tmp = flip(matrix, tmp, 2, 0, True, moves)
        tmp = flip(matrix, tmp, 2, 2, True, moves)
        tmp = flip(matrix, tmp, 3, 2, False, moves)
        flip(matrix, tmp, 3, 0, False, moves)
    else:
        if blank_pos[1] < t_col:
            tmp = flip(matrix, blank_pos, 3, 3, False, moves)
        else:
            tmp = flip(matrix, blank_pos, 1, 1, False, moves)
        tmp = flip(matrix, tmp, 2, 1, False, moves)
        tmp = flip(matrix, tmp, 2, 3, False, moves)
        tmp = flip(matrix, tmp, 1, 3, False, moves)
        tmp = flip(matrix, tmp, 2, 0, True, moves)
        flip(matrix, tmp, 3, 1, True, moves)


def remove_target(moves_map):
    for i in range(4):
        for j in range(4):
            if moves_map[i][j] == 2:
                moves_map[i][j] = 0
                break


def solution(position):
    moves = []
    if is_even_permutation(position[:-1]):
        moves_map = [[0] * 4 for _ in range(4)]
        matrix = get_matrix(position)
        while True:
            target_goal_pos = get_target_goal_pos(matrix, moves_map)
            target = goal_pos[target_goal_pos[0]][target_goal_pos[1]]
            if target == 0:
                break
            target_actual_pos = get_actual_pos(target, matrix)
            moves_map[target_actual_pos[0]][target_actual_pos[1]] = 2
            blank_pos = get_actual_pos(0, matrix)
            path = get_path(target_actual_pos, target_goal_pos, moves_map)
            if len(path) > 0:
                p = get_path(blank_pos, path[0], moves_map)
            else:
                p = []
            if len(p) == 0:
                resolve_collision(matrix, blank_pos, target_actual_pos[0],
                                  target_actual_pos[1], moves)
                remove_target(moves_map)
            else:
                move_along_path(p, blank_pos, target_actual_pos, matrix, moves,
                                moves_map)
    return moves


if __name__ == '__main__':
    # array = solution([1, 2, 3, 4, 5, 6, 7, 8, 13, 9, 11, 12, 10, 14, 15, 0])
    # array = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
    array = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 13, 14, 11, 0])
    # array = solution([6, 4, 13, 10,
    #                   9, 12, 15, 3,
    #                   14, 5, 11, 7,
    #                   2, 8, 1, 0])
    print(array)
