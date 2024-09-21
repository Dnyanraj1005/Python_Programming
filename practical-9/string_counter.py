def validate_string_counter(text):
    count = {"{": 0, "(": 0, "<": 0, "[": 0}
    order = []
    pairs = {"}": "{", ")": "(", ">": "<", "]": "["}

    for char in text:
        if char in count:
            count[char] += 1
            order.append(char)
        elif char in pairs:
            if count[pairs[char]] == 0 or order[-1] != pairs[char]:
                return "invalid"
            count[pairs[char]] -= 1
            order.pop()

    return "valid" if all(v == 0 for v in count.values()) else "invalid"


def validate_multiple_strings(strings):
    results = []
    for text in strings:
        result = validate_string_counter(text)
        results.append((text, result))
    return results

input_strings = ["{}", "([])", "{[}]", "<>", "}{", "[<>()]"]
results = validate_multiple_strings(input_strings)

for string, result in results:
    print(f"{string}: {result}")
