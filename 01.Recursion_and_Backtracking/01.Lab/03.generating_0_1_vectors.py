def generate_vector(index, vector):
    if index >= len(vector):
        print(*vector, sep='')
        return

    for n in range(2):
        vector[index] = n
        generate_vector(index + 1, vector)


n = int(input())
vector = [0] * n
generate_vector(0, vector)

