def count_sentences(filename):
    with open(filename, 'r') as file:
        text = file.read()

    sentence_endings = {'.', '!', '?'}
    count = 0
    in_sentence = False

    for char in text:
        if char not in sentence_endings and not in_sentence:
            in_sentence = True
        elif char in sentence_endings and in_sentence:
            count += 1
            in_sentence = False

    if in_sentence:
        count += 1

    return count

filename = 'input.txt'
num_sentences = count_sentences(filename)
print(num_sentences)