def repunctuate(sentence:str):
    sentence = sentence.split(" ")
    sentence = [i for i in sentence if i not in [',', ':', ';', '.','!', '?', '–', '"']] 
    return(" ".join(sentence))
