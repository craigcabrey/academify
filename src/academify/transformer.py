import nltk
import nltk.corpus
import nltk.tokenize
import textwrap
import tqdm

from .fluff import transitions


class Transformer():
    def __init__(self, mode, length, input, output):
        self.mode = mode
        self.source = input.read()
        self.target_length = length
        self.output = output
        self.buffer = ''
        self.transitions = transitions()

    def transform(self):
        sentences = nltk.tokenize.sent_tokenize(self.source)
        cur_len = len(self.buffer)

        while cur_len < self.target_length:
            for sentence in tqdm.tqdm(sentences):
                # TODO: develop sentence-level blacklist
                if '%%' in sentence:
                    self.buffer += sentence
                    continue

                words = nltk.tokenize.word_tokenize(sentence)

                # TODO: develop word-level blacklist
                # Extract only adjectives ('JJ')
                adjectives = [
                    tag[0] for tag in nltk.pos_tag(words)
                        if tag[1] == 'JJ' and not tag[0].startswith('\\')
                ]

                replacement_adjectives = {}
                for adjective in adjectives:
                    synonyms = set()
                    synonym_sets = nltk.corpus.wordnet.synsets(adjective)
                    for synonym_set in synonym_sets:
                        synonyms.update(synonym_set.lemma_names())

                    if len(synonyms) > 0:
                        replacement_adjectives[adjective] = max(synonyms, key=len)

                self.buffer += sentence

                if len(replacement_adjectives) > 0:
                    fluff = sentence[0].lower() + sentence[1:]
                    for original, replacement in replacement_adjectives.items():
                        fluff = fluff.replace(original, replacement)

                    fluff = next(self.transitions) + ', ' + fluff

                    # Time to make our audience proud
                    self.buffer += fluff

            cur_len = len(self.buffer)

    def save(self):
        self.output.write(self.buffer)
