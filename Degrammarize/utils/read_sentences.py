import json
import codecs
def get_sentences():
    json_file = codecs.open("utils/sentences.json", "r", "utf-8")
    json_obj = json.loads("\n".join(json_file.readlines()).encode('utf-8'))
    return(json_obj)
