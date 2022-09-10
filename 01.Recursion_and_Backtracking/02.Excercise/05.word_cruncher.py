def find_combination(target_string, elements, combination):
    if target_string == '':
        print(' '.join(combination))
        return

    for element in elements:
        if target_string.startswith(element):
            combination.append(element)
            new_elements = list(elements)
            new_elements.remove(element)
            find_combination(target_string[len(element):], new_elements, combination)
            combination.pop()


elements = list(input().split(', '))
target_string = input()

find_combination(target_string, elements, [])
