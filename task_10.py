def count_words(string):
    word_counts = {}
    current_word = []
    
    for char in string.lower():
        if char.isalpha() or char == "'":
            current_word.append(char)
        else:
            if current_word:
                word = ''.join(current_word)
                word_counts[word] = word_counts.get(word, 0) + 1
                current_word = []
    
    if current_word:
        word = ''.join(current_word)
        word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts


#Done