def count_occurrences(target_char, input_string):
    count = 0
    start_index = 0

    while True:
        index = input_string.find(target_char, start_index)
        if index == -1:
            break
        count += 1
        start_index = index + 1

    return count

fruit = "banana"
char_to_count = "a"
result = count_occurrences(char_to_count, fruit)
print(result)
