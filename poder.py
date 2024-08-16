import math
[N, M] = [int(x) for x in input().split(" ")]

board = [[int(x) for x in input().split(" ")] for _ in range(N)]

ortogonal_offsets = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
    ]

def moves_from(i: int, j: int, my_power: int, curr_board)  :
    moves = []

    for m in ortogonal_offsets:
        if i+m[0] >= N or j+m[1] >= M or i+m[0] < 0 or j+m[1] < 0:
            continue 

        p = curr_board[i+m[0]][j+m[1]]
        if p > my_power:
            continue

        if p == 0:
            curr_board[i][j] = math.inf
            moves += moves_from(i+m[0], j+m[1], my_power, curr_board)
            curr_board[i][j] = 0
        else:
            moves.append((i+m[0], j+m[1]))
    return moves

hero_cache = {}
def get_max_heroi(i: int, j: int) -> int:
    start = [board[x[0]][x[1]] for x in moves_from(i, j, board[i][j], board)]
    for m in start:
        if m in hero_cache:
            return hero_cache[m] 


    board_copy = [[x for x in linha] for linha in board]

    posi = i
    posj = j
    power = board_copy[i][j]
    board_copy[i][j] = 0
    while True:
        moves = moves_from(posi, posj, power, board_copy)
        if len(moves) == 0 or all(board_copy[x[0]][x[1]] == 0 for x in moves):
            hero_cache[(i*10)+j] = power
            return power
        move = min(moves, key=lambda x: board_copy[x[0]][x[1]] if board_copy[x[0]][x[1]] > 0 else math.inf)
        power += board_copy[move[0]][move[1]]
        posi = move[0]
        posj = move[1]
        board_copy[move[0]][move[1]] = 0


answer = [[get_max_heroi(i, j) for j in range(M)] for i in range(N)]

for i, linha in enumerate(answer):
    for e in linha:
        print(f"{e} ", end="")
    if i < N-1:
        print()