def find_paths(row, col, rows, columns):
    result = 0
    if row >= rows or col >= columns:
        return 0

    if row == rows - 1 and col == columns - 1:
        return 1

    result += find_paths(row, col + 1, rows, columns)
    result += find_paths(row + 1, col, rows, columns)

    return result


rows = int(input())
columns = int(input())
print(find_paths(0, 0, rows, columns))


