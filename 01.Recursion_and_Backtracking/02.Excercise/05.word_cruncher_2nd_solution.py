def find_combinations(index, target_string, words_by_idx, words_count, combinations):
    if index >= len(target_string):
        print(' '.join(combinations))
        return
    if index not in words_by_idx:
        return

    for word in words_by_idx[index]:
        if words_count[word] == 0:
            continue
        combinations.append(word)
        words_count[word] -= 1

        find_combinations(index + len(word), target_string, words_by_idx, words_count, combinations)

        combinations.pop()
        words_count[word] += 1


elements = input().split(', ')
target_string = input()

words_by_idx = {}
words_count = {}

for element in elements:
    if element not in words_count:
        words_count[element] = 0

    words_count[element] += 1

    try:
        index = 0
        while True:

            index = target_string.index(element, index)

            if index not in words_by_idx:
                words_by_idx[index] = set()
            words_by_idx[index].add(element)
            index += len(element)
    except ValueError:
        pass

find_combinations(0, target_string, words_by_idx, words_count, [])
