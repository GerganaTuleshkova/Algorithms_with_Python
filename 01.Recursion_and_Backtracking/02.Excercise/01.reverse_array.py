# def reverse_array(initial_list, result_list):
#     if len(initial_list) == 0:
#         print(' '.join(result_list))
#         return
#     last_element = initial_list.pop()
#     result_list.append(last_element)
#     reverse_array(initial_list, result_list)
#
# second solution

def reverse_array(index, given_list):
    if index == len(given_list) // 2:
        print(' '.join(given_list))
        return
    index_to_swap = len(given_list) - 1 - index
    given_list[index], given_list[index_to_swap] = given_list[index_to_swap], given_list[index]
    reverse_array(index + 1, given_list)


given_list = input().split(' ')
# reverse_array(given_list, [])
reverse_array(0, given_list)

