# task1
def display_file_content(daniya):
    with open(daniya, 'r') as file:
        for line in file:
            print(line)

# task2
import random

def read_random_line(daniya):
    with open(daniya, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        return random_line

# task3
def count_uppercase_characters(daniya):
    with open(daniya, 'r') as file:
        content = file.read()
        uppercase_count = sum(1 for char in content if char.isupper())
        return uppercase_count

# task4
def count_lines_not_starting_with_D(daniya):
    with open(daniya, 'r') as file:
        lines = file.readlines()
        count = sum(1 for line in lines if not line.strip().startswith('D'))
        return count

# task4
def count_words_ending_with_F(daniya):
    with open(daniya, 'r') as file:
        words = file.read().split()
        count = sum(1 for word in words if word.lower().endswith('f'))
        return count

# task5
def count_specific_words(daniya):
    with open(daniya, 'r') as file:
        content = file.read()
        all_count = content.count('all')
        none_count = content.count('none')
        return all_count, none_count

# tak6
from collections import Counter

def count_word_frequency(daniya):
    with open(daniya, 'r') as file:
        words = file.read().split()
        word_frequency = Counter(words)
        return word_frequency

# task7
def find_longest_word(daniya):
    with open(daniya, 'r') as file:
        words = file.read().split()
        longest_word = max(words, key=len)
        return longest_word

# task8
def replace_B_with_J(daniya):
    with open(daniya, 'r') as file:
        content = file.read()
        corrected_content = content.replace('B', 'J')
        return corrected_content

# task9
def count_A_and_B_occurrences(daniya):
    with open(daniya, 'r') as file:
        content = file.read().lower()
        a_count = content.count('a')
        b_count = content.count('b')
        return f'a={a_count}, b={b_count}'
