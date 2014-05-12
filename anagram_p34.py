#!/usr/bin/env python3

'''This program takes a word from user and returns all anagrams of that word found in /users/abrick/resources/american-english-insane dictionary'''

def dump_dictionary():
    import pickle
    outf = open('dict.pkl','wb')
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
        else:
            word_dict[wl]={kw:[w]}
      
    pickle.dump(word_dict,outf)
    outf.close()

def load_dictionary():
    import pickle
    inputf = open('dict.pkl','rb')
    return pickle.load(inputf)

try:
    print("Loading dictionary.")
    word_dict=load_dictionary()
except:
    print("I'm dumping the dictionary")
    dump_dictionary()
    word_dict=load_dictionary()

while 1:
    input_word = input('Enter a word to find its anagram or enter q to quit: ')
    if input_word == '':
        print("I'm dumping the dictionary")
        dump_dictionary()
    if input_word == 'q':
        exit()

    result = []
    word_letters = sorted(input_word)

    try:
        a=word_dict[len(input_word)]
        try:
            a=word_dict[len(input_word)][word_letters[0]]
        except KeyError:
            continue
    except KeyError:
        continue
               
    for word in word_dict[len(input_word)][word_letters[0]]:
 
        if sorted(word) == word_letters:
            result.append(word)
    for r in result:
        print(r)
