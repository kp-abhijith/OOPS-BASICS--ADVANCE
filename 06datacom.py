
def lz77_compress(text, window_size=20, lookahead_size=15):
    result = []
    i = 0

    while i < len(text):
        start = max(0, i - window_size)
        window = text[start:i]

        best_length = 0
        best_distance = 0

        for j in range(len(window)):
            length = 0

            while (
                length < lookahead_size
                and i + length < len(text)
                and j + length < len(window)
                and window[j + length] == text[i + length]
            ):
                length += 1

            if length > best_length:
                best_length = length
                best_distance = len(window) - j

        if best_length > 0:
            next_pos = i + best_length

            if next_pos < len(text):
                next_char = text[next_pos]
                result.append(
                    (best_distance, best_length, next_char)
                )
                i = next_pos + 1

            else:
                result.append(
                    (best_distance, best_length, "")
                )
                i = next_pos

        else:
            result.append((0, 0, text[i]))
            i += 1

    return result


# ==========================================================
# LZ78
# ==========================================================

def lz78_compress(text):
    dictionary = {}
    next_index = 1
    result = []
    current = ""
    i = 0

    while i < len(text):
        current += text[i]

        if current not in dictionary:
            if len(current) == 1:
                prefix = ""
            else:
                prefix = current[:-1]

            index = dictionary.get(prefix, 0)
            character = current[-1]

            result.append((index, character))

            dictionary[current] = next_index
            next_index += 1
            current = ""

        i += 1

    if current:
        index = dictionary.get(current, 0)
        result.append((index, ""))

    return result


text = input("Enter text: ")

# LZ77
lz77_result = lz77_compress(text)

print("\nLZ77 Output:")
for item in lz77_result:
    print(item)

print("Number of LZ77 tuples:", len(lz77_result))


# LZ78
lz78_result = lz78_compress(text)

print("\nLZ78 Output:")
for item in lz78_result:
    print(item)

print("Number of LZ78 tuples:", len(lz78_result))


print("\nOriginal characters:", len(text))
print("LZ77 tuples:", len(lz77_result))
print("LZ78 tuples:", len(lz78_result))
