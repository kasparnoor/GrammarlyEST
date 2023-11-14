import json

def get_sentences():
    json_file = open("utils/sentences.json", 'r')
    json_obj = json.loads("\n".join(json_file.readlines()))
    return(json_obj)
