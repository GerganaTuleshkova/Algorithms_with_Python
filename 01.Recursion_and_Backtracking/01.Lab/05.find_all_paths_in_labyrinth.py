def find_paths(row, col, labyrinth, direction, path):
    # print(f'Now checking with row {row} and col {col}, path so far is {path}')
    if row < 0 or col < 0 or row >= len(labyrinth) or col >= len(labyrinth[0]):
        # print('This recursion calling ends as move is outside labyrinth')
        return
    if labyrinth[row][col] == '*':
        # print('This recursion calling ends as move is hitting the wall')
        return
    if labyrinth[row][col] == 'v':
        # print('This recursion calling ends as move is to a cell that was visited')

        return
    # print(f'This move is valid, appending to path the move - {direction}')
    path.append(direction)

    if labyrinth[row][col] == 'e':
        print(''.join(path))
    else:
        labyrinth[row][col] = 'v'
        # print('Now will try move to the R')

        find_paths(row, col + 1, labyrinth, 'R', path)
        # print('Now will try move to the L')

        find_paths(row, col - 1, labyrinth, 'L', path)
        # print('Now will try move to the D')

        find_paths(row + 1, col, labyrinth, 'D', path)
        # print('Now will try move to the U')

        find_paths(row - 1, col, labyrinth, 'U', path)
        # print(f'Tried all moves, now marking the cell {row} {col} as "-"')

        labyrinth[row][col] = '-'
    path.pop()


row_size = int(input())
column_size = int(input())
labyrinth = []

for _ in range(row_size):
    labyrinth.append(list(input()))

find_paths(0, 0, labyrinth, '', [])
