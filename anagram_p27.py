
from sys import argv

def dump_dictionary():

    import cPickle
    outf = open('dict.pkl','wb')

    with open('dictionary', 'r') as fh:
        word_list = [word.strip('\n') for word in fh.readlines()]

    cPickle.dump(word_list,outf)
    outf.close()

def load_dictionary():
    import cPickle
    inputf = open('dict.pkl','rb')
    return cPickle.load(inputf)

try:
  input = argv[1]
except:
  print "I'm dumping the dictionary"
  dump_dictionary()
  exit()


result = []
word_letters = sorted(input)
for word in load_dictionary():
    if sorted(word) == word_letters:
        result.append(word)
for r in result:
    print r
