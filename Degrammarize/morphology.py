from estnltk import Text

from utils.read_sentences import get_sentences
def morph(list_of_words:list[str]):
    return(list_of_words)

sentence = Text(get_sentences()["1"])
#print(repunctuate(sentence))
print(sentence.morph_analysis[0:4, 'root'])

