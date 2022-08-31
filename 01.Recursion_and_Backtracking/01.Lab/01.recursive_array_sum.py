def calc_list_sum(list_of_nums, index):
    if index == len(list_of_nums) - 1:
        return list_of_nums[index]
    return list_of_nums[index] + calc_list_sum(list_of_nums, index + 1)


my_list = [int(n) for n in input().split(' ')]
result = (calc_list_sum(my_list, 0))
print(result)
