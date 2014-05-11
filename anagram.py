#!/usr/bin/env python3

from sys import argv

input = argv[1]

with open('dictionary', 'r') as fh:
    word_list = [word.strip('\n') for word in fh.readlines()]

result = []
word_letters = sorted(input)
for word in word_list:
    if sorted(word) == word_letters:
        result.append(word)
for r in result:
    print(r)
