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
    while True:
        yield random.choice(transition_phrases)
