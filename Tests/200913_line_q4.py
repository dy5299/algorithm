def solution(maze):
    import numpy as np
    nsize = len(maze)
    maze = np.array(maze)
    temp = np.ones((nsize + 2, nsize + 2), dtype=int)
    temp[1:-1, 1:-1] = maze
    maze = temp

    present = np.array([1, 1])
    count = 0

    # 처음
    if maze[1, 2] == 1:
        direc = 'down'
        present[0] += 1
        count += 1
    elif maze[2, 1] == 1:
        direc = 'right'
        present[1] += 1
        count += 1

    def right(direc, present, count):
        direc = 'right'
        present[1] += 1
        count += 1
        return direc, present, count

    def left(direc, present, count):
        direc = 'left'
        present[1] -= 1
        count += 1
        return direc, present, count

    def down(direc, present, count):
        direc = 'down'
        present[0] += 1
        count += 1
        return direc, present, count

    def up(direc, present, count):
        direc = 'up'
        present[0] -= 1
        count += 1
        return direc, present, count

    direcarr = ['down', 'right', 'up', 'left']
    # 움직이는 방향은 다 가능. 왼쪽손에 막혔냐 안 막혔냐

    while True:
        if present[0] == nsize and present[1] == nsize:
            break

        if direc == 'down':
            if maze[present[0], present[1] + 1] != 1:  # 오른쪽 없으면 오른
                direc, present, count = right(direc, present, count)
            elif maze[present[0] + 1, present[1]] != 1:  # 아래 없으면 아래
                direc, present, count = down(direc, present, count)
            elif maze[present[0], present[1] - 1] != 1:  # 왼 없으면 왼
                direc, present, count = left(direc, present, count)
            elif maze[present[0] - 1, present[1]] != 1:  # 위 없으면 위
                direc, present, count = up(direc, present, count)

        elif direc == 'right':
            if maze[present[0] - 1, present[1]] != 1:  # 위 없으면 위로
                direc, present, count = up(direc, present, count)
            elif maze[present[0], present[1] + 1] != 1:  # 오른 없으면 오른
                direc, present, count = right(direc, present, count)
            elif maze[present[0] + 1, present[1]] != 1:  # 아래 없으면 아래
                direc, present, count = down(direc, present, count)
            elif maze[present[0], present[1] - 1] != 1:  # 왼 없으면 왼
                direc, present, count = left(direc, present, count)


        elif direc == 'up':
            if maze[present[0], present[1] - 1] != 1:  # 왼 없으면 왼
                direc, present, count = left(direc, present, count)
            elif maze[present[0] - 1, present[1]] != 1:  # 위 없으면 위로
                direc, present, count = up(direc, present, count)
            elif maze[present[0], present[1] + 1] != 1:  # 오른 없으면 오른
                direc, present, count = right(direc, present, count)
            elif maze[present[0] + 1, present[1]] != 1:  # 아래 없으면 아래
                direc, present, count = down(direc, present, count)


        elif direc == 'left':
            if maze[present[0] + 1, present[1]] != 1:  # 아래 없으면 아래
                direc, present, count = down(direc, present, count)
            elif maze[present[0], present[1] - 1] != 1:  # 왼 없으면 왼
                direc, present, count = left(direc, present, count)
            elif maze[present[0] - 1, present[1]] != 1:  # 위 없으면 위로
                direc, present, count = up(direc, present, count)
            elif maze[present[0], present[1] + 1] != 1:  # 오른 없으면 오른
                direc, present, count = right(direc, present, count)

    answer = count
    return answer