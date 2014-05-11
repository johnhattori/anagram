#!/usr/bin/env python3

from sys import argv

def dump_dictionary():

    import pickle
    outf = open('dict.pkl','wb')
    

    word_dict={}
    fh=open('dictionary', 'r')
    for line in fh:
        w=line.strip('\n')
        wl=len(w)
        if wl in word_dict:
            word_dict[wl].append(w)
        else:
            word_dict[wl]=[w]

    pickle.dump(word_dict,outf)
    outf.close()

def load_dictionary():
    import pickle
    inputf = open('dict.pkl','rb')
    return pickle.load(inputf)

try:
  input = argv[1]
except:
  print("I'm dumping the dictionary")
  dump_dictionary()
  exit()


result = []
word_letters = sorted(input)
word_dict=load_dictionary()
for word in word_dict[len(input)]:
    if sorted(word) == word_letters:
        result.append(word)
for r in result:
    print(r)
