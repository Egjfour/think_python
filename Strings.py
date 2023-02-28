# EXERCISE 8-2 - count the number of "a" characters in banana

fruit = 'banana'
answer = 'The number of a\'s is {0}'.format(fruit.count('a'))
print(answer)


# EXERCISE 8-3 - Create the is_palindrome function using string slicers


def is_palindrome(word):
    """
    Checks if the provided word is a palindrome using string slicers

    :param word: str - the word to check
    :return: bool - whether the string is a palindrome
    """

    answer = word == word[::-1]
    return answer


test_word = 'racecar'  # Returns true
# test_word = 'cat' # Returns false
mapping = {'word': test_word, 'answer': is_palindrome(test_word)}
print('Is {word} a palindrome? {answer}'.format_map(mapping))


# EXERCISE 8-5 - Create a Caesar Cypher

def encrypt_caesar(input: str, rotation: int):
    """
    Encrypts a provided string to a caesar cypher by rotating the characters by a fixed amount

    :param input: str - the string to rotate
    :param rotation: int - number of positions to rotate by
    :return: str - the original string with caesar encrytion applied
    """

    reformatted = input.lower()

    encrypted_codes = [ord(char) + rotation for char in reformatted]

    encrypted_string = ''.join([chr(x) for x in encrypted_codes])

    return encrypted_string


print(encrypt_caesar('Cheer', 7))

# Chapter 9: Case Study: Word Play

words = open("C:/repos/words.txt")


def print_words(file):
    for line in file:
        line_stripped = line.strip()
        if len(line_stripped) > 20:
            print(line_stripped)


# print_words(words)


def has_no_e(file):
    all_words = []
    words_no_e = []
    for line in file:
        word = line.strip()
        all_words.append(word)
        if "e" not in word.lower():
            words_no_e.append(word)
    return all_words, words_no_e


# word_list, words_without_e = has_no_e(words)
#
# print("Number of words without e is " + str(len(words_without_e)) + " which is ",
#       str(round(len(words_without_e) / len(word_list) * 100)) + "% of all words")


def avoids(word, forbidden_letters):
    for letter in word.lower():
        if letter in forbidden_letters.lower():
            return False
    return True


def count_avoids(file, forbidden_letters):
    count = 0
    for line in file:
        if avoids(line.strip(), forbidden_letters):
            count += 1
    return count


# print(avoids("Rouge", "tq"))
print(count_avoids(words, "x"))

