import nltk.tokenize

class Transformer():
    def __init__(self, mode, length, input, output):
        self.buffer = ''.join(input.readlines())

    def transform(self):
        sentences = nltk.tokenize.sent_tokenize(self.buffer)

    def save(self):
        pass

