import sys
import os

def print_hello_world():
    print("Hello, World!")

def reverse_string(string):
    print(string[::-1])

def count_word_frequency(filename):
    word_freq = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.lower()
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1

    print("Word Frequency:")
    for word, frequency in word_freq.items():
        print(f"{word}: {frequency}")

if len(sys.argv) == 1:
    print_hello_world()
elif len(sys.argv) == 2:
    arg = sys.argv[1]
    if os.path.isfile(arg):
        count_word_frequency(arg)
    else:
        reverse_string(arg)
else:
    print("Invalid number of arguments.")
