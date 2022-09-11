def quick_sort(start_index, end_index, numbers):
    if start_index >= end_index:
        return

    pivot_index = start_index
    left_index = start_index + 1
    right_index = end_index

    while left_index <= right_index:
        if numbers[left_index] > numbers[pivot_index] > numbers[right_index]:
            numbers[left_index], numbers[right_index] = numbers[right_index], numbers[left_index]

        if numbers[left_index] <= numbers[pivot_index]:
            left_index += 1

        if numbers[right_index] >= numbers[pivot_index]:
            right_index -= 1
    numbers[pivot_index], numbers[right_index] = numbers[right_index], numbers[pivot_index]
    quick_sort(start_index, right_index - 1, numbers)
    quick_sort(left_index, end_index, numbers)


numbers = [int(x) for x in input().split()]
quick_sort(0, len(numbers) - 1, numbers)
print(*numbers, sep=' ')
