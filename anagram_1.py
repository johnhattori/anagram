#!/usr/bin/env python3

from sys import argv

input = argv[1]

def dump_dictionary():

    import pickle
    outf = open('dict.pkl','wb')

    with open('dictionary', 'r') as fh:
        word_list = [word.strip('\n') for word in fh.readlines()]

    pickle.dump(word_list,outf)
    outf.close()

def load_dictionary():
    import pickle
    inputf = open('dict.pkl','rb')
    return pickle.load(inputf)


result = []
word_letters = sorted(input)
for word in load_dictionary():
    if sorted(word) == word_letters:
        result.append(word)
for r in result:
    print(r)
