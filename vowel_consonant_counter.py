#!/usr/local/bin/python3

def find(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    vowel_counts = {}
    consonant_counts = {}
    invalid_characters = {}

    #intialize vowels
    for v in vowels:
        vowel_counts[v] = 0

    #intialize consonants 
    for c in consonants:
        consonant_counts[c] = 0

    for word in words:
        for letter in word:
            if letter in vowels:
                vowel_counts[letter] += 1
            elif letter in consonants:
                consonant_counts[letter] += 1
            else:
                if not (letter in invalid_characters.keys()):
                    invalid_characters[letter] = 0
                invalid_characters[letter] += 1

    result = {
            "vowels": vowel_counts,
            "consonants": consonant_counts,
            "other": invalid_characters
            }

    print(result)
    return result
