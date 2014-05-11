#!/usr/bin/env python3

from sys import argv

input = argv[1]

word_dict={}
fh=open('dictionary', 'r')
for line in fh:
    w=line.strip('\n')
    wl=len(w)
    kw=sorted(w)[0]
    if wl in word_dict:
        if kw in word_dict[wl]:
            word_dict[wl][kw].append(w)
        else:
            word_dict[wl][kw]=[w]
    else:                                                    word_dict[wl]={kw:[w]}

result = []
word_letters = sorted(input)

for word in word_dict[len(input)][word_letters[0]]:
    if sorted(word) == word_letters:
        result.append(word)
for r in result:
    print(r)
