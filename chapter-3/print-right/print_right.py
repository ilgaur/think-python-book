def print_right(text):
    word_length = len(text)
    offset = 40 - word_length
    print(offset * ' ', end='')
    print(text)

print_right("Hello!")