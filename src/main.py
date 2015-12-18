#!/usr/bin/env python3

import argparse

import academify


def process_arguments():
    parser = argparse.ArgumentParser(
        description='''
            Automatically inflate a LaTeX paper to meet an arbitrary
            character or minimum word requirement sometimes imposed by
            academia.
        '''
    )

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s {version}'.format(version=academify.__version__)
    )

    parser.add_argument(
        '-c',
        '--characters',
        action='store_true',
        help='Use characters to calculate the minimum length requirement'
    )

    parser.add_argument(
        'length',
        type=int,
        help='Minimum length requirement (defaults to words)'
    )

    parser.add_argument(
        'input',
        type=argparse.FileType('r'),
        help='LaTeX file to be processed'
    )

    parser.add_argument(
        'output',
        type=argparse.FileType('w'),
        help='Output file destination'
    )

    return parser.parse_args()

def main():
    args = process_arguments()

    config = {
        'mode': academify.CHARACTERS if args.characters else academify.WORDS,
        'length': args.length,
        'input': args.input,
        'output': args.output
    }

    transformer = academify.Transformer(**config)
    transformer.transform()
    transformer.save()

if __name__ == '__main__':
    main()
