def binary_search(numbers, target):
    left_idx = 0
    right_idx = len(numbers) - 1

    while True:
        if left_idx > right_idx:
            return -1
            break

        mid_idx = (left_idx + right_idx) // 2
        mid_element = numbers[mid_idx]

        if mid_element == target:
            return mid_idx

        if mid_element < target:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1


numbers = [int(x) for x in input().split()]
target_number = int(input())

print(binary_search(numbers, target_number))
