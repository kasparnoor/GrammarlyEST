from utils.read_sentences import get_sentences
from repunctuate import repunctuate
from morphology import 
def main():
    for sentence in get_sentences().values():
        # Remove all punctuation
        sentence_wrong = repunctuate(sentence)
        # Mess up the forms of words
        sentence_wrong = 
        print(sentence, "--->", sentence_wrong)
        print()
if __name__ == "__main__":
    main()