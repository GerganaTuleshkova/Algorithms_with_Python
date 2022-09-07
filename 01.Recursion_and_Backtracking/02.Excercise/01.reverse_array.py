def reverse_array(initial_list, result_list):
    if len(initial_list) == 0:
        print(' '.join(result_list))
        return
    last_element = initial_list.pop()
    result_list.append(last_element)
    reverse_array(initial_list, result_list)


given_list = list(input().split(' '))
reverse_array(given_list, [])
