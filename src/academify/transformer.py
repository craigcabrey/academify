from .fluff import transitions
import nltk.tokenize


class Transformer():
    def __init__(self, mode, length, input, output):
        self.mode = mode
        self.source = input.read()
        self.target_length = length
        self.output = output
        self.buffer = ''

    def transform(self):
        sentences = nltk.tokenize.sent_tokenize(self.source)
        cur_len = len(self.buffer)

        while cur_len < self.target_length:
            for sentence in sentences:
                self.buffer += sentence
            cur_len = len(self.buffer)

    def save(self):
        self.output.write(self.buffer)
