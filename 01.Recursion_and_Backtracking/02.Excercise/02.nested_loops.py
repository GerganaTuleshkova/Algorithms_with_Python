def nested_loops(index, vector):
    if index >= len(vector):
        print(*vector, sep=' ')
        return

    for n in range(1, len(vector) + 1):
        vector[index] = n
        nested_loops(index + 1, vector)


n = int(input())
vector = [1] * n
nested_loops(0, vector)
