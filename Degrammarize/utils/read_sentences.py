import json

def get_sentences():
    json_file = open("Degrammarize/utils/sentences.json", 'r')
    json_obj = json.loads(json_file)
    return(json_obj)
