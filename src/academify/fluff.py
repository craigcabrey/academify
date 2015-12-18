import random


transition_phrases = [
    'In summary',
    'In other words',
    'More precisely',
    'In conclusion',
    'To put it differently',
    'Furthermore',
    'In addition',
    'Likewise',
    'Moreover',
    'To rephase it',
    'By the same token',
    'Subsequently',
    'Additionally',
    'Similarly',
    'Equally important',
    'That is to say',
    'To put it another way',
    'That is',
    'Even more',
    'To emphasize',
    'In fact'
]

def transitions():
    previous_phrase = None
    while True:
        next_phrase = random.choice(transition_phrases)
        while next_phrase is previous_phrase:
            next_phrase = random.choice(transition_phrases)

        previous_phrase = next_phrase
        yield next_phrase
