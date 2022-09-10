def find_paths(row, col, labyrinth, path_count):
    result = 0
    if row < 0 or col < 0 or row >= len(labyrinth) or col >= len(labyrinth[0]):
        return 0
    if labyrinth[row][col] == 'v':
        return 0

    if row == (len(labyrinth) - 1) and col == (len(labyrinth[0]) - 1):
        path_count += 1
        return 1
    else:
        labyrinth[row][col] = 'v'

        result += find_paths(row, col + 1, labyrinth, path_count)
        result += find_paths(row + 1, col, labyrinth, path_count)

        labyrinth[row][col] = '-'
        return result


row_size = int(input())
column_size = int(input())
labyrinth = []

for _ in range(row_size):
    labyrinth.append(['-' for _ in range(column_size)])

print(find_paths(0, 0, labyrinth, 0))


