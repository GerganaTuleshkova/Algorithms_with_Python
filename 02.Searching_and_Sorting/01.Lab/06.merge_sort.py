def merge_lists(left_list, right_list):
    result = [None] * (len(left_list + right_list))
    left_index = 0
    right_index = 0
    result_index = 0

    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            result[result_index] = left_list[left_index]
            left_index += 1
        else:
            result[result_index] = right_list[right_index]
            right_index += 1
        result_index += 1

    while left_index < len(left_list):
        result[result_index] = left_list[left_index]
        left_index += 1
        result_index += 1

    while right_index < len(right_list):
        result[result_index] = right_list[right_index]
        right_index += 1
        result_index += 1
    return result


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    middle_index = len(numbers) // 2
    left_part = numbers[:middle_index]
    right_part = numbers[middle_index:]

    return merge_lists(merge_sort(left_part), merge_sort(right_part))


numbers = [int(x) for x in input().split()]

print(*merge_sort(numbers), sep=' ')
