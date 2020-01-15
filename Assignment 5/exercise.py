# Programming Exercises (Files)
# 1. A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the works of an author, or in a single text.
# Define a function that given the file name of a text will return all its hapaxes.
# Make sure your program ignores capitalization.
# [open http://www.gutenberg.org/  and download an e-book as plain text, use the file for texting your program]
#
# 2. Write a program that given a text file will create a new text file in which all the lines from the original file are
# numbered from 1 to n (where n is the number of lines in the file).
#
# 3. Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).
# [open http://www.gutenberg.org/  and download an e-book as plain text, use the file for texting your program]
#
# 4. A certain children’s game involves starting with a word in a particular category. Each participant in turn says a word,
# but that word must begin with the final letter of the previous word. Once a word has been given, it cannot be repeated.
# If an opponent cannot give a word in the category, they fall out of the game.
#
# For example, with "animals" as the category, Child 1: dog  Child 2: goldfish Child 1: hippopotamus Child 2: snake ...
# Your task in this exercise is as follows: Take the following selection of 70 English Pokemon names and generate the/a sequence with the highest possible number
# of Pokemon names where the subsequent name starts with the final letter of the preceding name. No Pokemon name is to be repeated.
#
# Ex 5 is up to come

# tool to get file descriptor
def getText(name):
    fd = open(name, 'r')
    content = fd.read()
    fd.close()
    return content.lower()

# EX 1
# récupère la fréquence dans un texte.
def getWordsFrequencies(text):
    frequencies = {}
    for word in text.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

# EX 1

# fonction qui permet de récuprerer les occurences d'un mot dans un texte
def getHapax(frequencies):
    hapax = []
    for word, freq in frequencies.items():
        if freq == 1:
            print(word, freq)
            hapax.append(word)
    return hapax

# EX 2
# le nom de la fonction parle d'elle même
def number_text(name):
    lines = getText(name)
    n = 1
    new_file = open("numerbed_" + name, 'w')
    for line in lines:
        new_file.write(str(n) + " " + line + "\n")
        n += 1
    new_file.close()

# EX 3
# Nom explicite
def getAverageLen(name):
    nb_word = 0
    total_len = 0
    text = getText(name)
    for word in text:
        nb_word += 1
        total_len += len(word)
    return total_len / nb_word

# EX 1
# nom explicite.
def hapaxFinder(name):
    text = getText(name)
    frequencies = getWordsFrequencies(text)
    return getHapax(frequencies)

# EX4 POKEMON - YAY -
def getPokemons():
    fd = open("pokemon_list.txt", 'r')
    content = fd.read()
    fd.close()
    return content.split()

def getSequence(start_index, pokemons):
    sequence = []
    current = pokemons[start_index]
    sequence.append(current)
    n = 0
    while n < len(pokemons):
        pokemon = pokemons[n]
        if pokemon not in sequence and pokemon[0] == current[-1]:
            current = pokemon
            sequence.append(current)
            n = 0
        n += 1
    return sequence

def getLongSq():
    pokemons = getPokemons()
    sequences = []
    n = 0
    while n < len(pokemons):
        sequences.append(getSequence(n, pokemons))
        n += 1
    return max(sequences, key=len)
