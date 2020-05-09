import pprint

pp = pprint.PrettyPrinter().pprint

import numpy as np

routes = []  # prestep direction, current position x, y
# route.append()
board = np.array([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]])
size = len(board)
board_new = np.ones((size + 1, size + 1))
board_new[:-1, :-1] = board


def findnext(board, routes, i, j):
    size = len(board)
    if board[i + 1, j] == 0 and board[i, j + 1] == 1:
        routes[-1].append([i + 1, j, 'down'])

    elif board[i + 1, j] == 1 and board[i, j + 1] == 0:
        routes[-1].append([i, j + 1, 'right'])

    elif board[i + 1, j] == 1 and board[i, j + 1] == 1:
        if i == size - 1 and j == size - 1:
            return routes
        else:
            del routes[-1]

    else:  # 둘 다 뚫려있으면
        routes[-1].append([i + 1, j, 'down'])
        routes.append(routes[-1][:-1])
        routes[-1].append([i, j + 1, 'right'])

    return routes


size = len(board[0])

routes.append([[0, 0, None]])
routes = findnext(board_new, routes, 0, 0)  # routes 첫번째

while True:
    if len(rows_idx) == 0: continue
    rows_idx = [x[-1][0] for x in routes]
    cols_idx = [x[-1][1] for x in routes]
    if sum(rows_idx) / len(rows_idx) >= size - 1 and sum(cols_idx) / len(cols_idx) >= size - 1:
        break
    routes = findnext(board_new, routes, routes[-1][-1][0], routes[-1][-1][1])  # routes 재귀

pp(routes)