numbers = [int(x) for x in input().split()]

for index in range(len(numbers)):
    min_index = index

    for current_index in range(index + 1, len(numbers)):
        if numbers[current_index] < numbers[min_index]:
            min_index = current_index
    numbers[index], numbers[min_index] = numbers[min_index], numbers[index]


print(*numbers, sep=' ')
