def find_duplicate_chars_count(s: str) -> dict:
    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    result = {}

    for char in count:
        if count[char] > 1:
            result[char] = count[char]

    return result


print(find_duplicate_chars_count("programming"))
print(find_duplicate_chars_count("mississippi"))
print(find_duplicate_chars_count("abcdefgh"))
print(find_duplicate_chars_count("abacabad"))