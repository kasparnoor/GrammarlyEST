import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'utils')))
print(sys.path)
from utils.read_sentences import get_sentences
def repunctuate(list_of_words:list[str]):
    return(list_of_words.remove(','))

sentence = get_sentences()[0]
repunctuate(sentence)