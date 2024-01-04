def count_occurrences(target_char, input_string):
    count = 0
    for char in input_string:
        if char == target_char:
            count += 1
    return count

fruit = "banana"
char_to_count = "a"
result = count_occurrences(char_to_count, fruit)
print(result)
