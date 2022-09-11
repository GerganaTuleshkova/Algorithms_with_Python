numbers = [int(x) for x in input().split()]

is_sorted = False
filled_counter = 0

while not is_sorted:
    is_sorted = True

    for index in range(1, len(numbers) - filled_counter):
        if numbers[index] < numbers[index - 1]:
            numbers[index], numbers[index - 1] = numbers[index - 1], numbers[index]
            is_sorted = False
    filled_counter += 1

print(*numbers, sep=' ')
