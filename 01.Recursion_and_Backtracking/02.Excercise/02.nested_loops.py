def nested_loops(index, limit, vector):
    if index >= len(vector):
        print(*vector, sep=' ')
        return

    for n in range(1, limit + 1):
        vector[index] = n
        nested_loops(index + 1, limit, vector)


n = int(input())
vector = [1] * n
nested_loops(0, n, vector)
