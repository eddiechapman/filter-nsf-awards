"""
filter_abstracts.py

Search NSF award abstracts for matching keywords.
"""
import pathlib
from nltk import sent_tokenize, word_tokenize
from nltk.util import ngrams

PATH_AWARD_DATA = pathlib.Path('award_data.txt')
PATH_SEARCH_TERMS = pathlib.Path('search_terms.txt')


def main():
    with open(PATH_SEARCH_TERMS, 'r') as f:
        search_terms = [line.strip().lower() for line in f]

    with open(PATH_AWARD_DATA, 'r') as f:
        award_data = [line for line in f]

    # determines maximum ngram size
    n = max({len(line.split()) for line in search_terms})

    for text in award_data:
        cell_phrases = set()
        for sentence in sent_tokenize(text):
            tokens = word_tokenize(sentence.lower())
            for i in range(n + 1):
                cell_phrases.update([' '.join(ng) for ng in ngrams(tokens, i)])

        query_matches = cell_phrases.intersection(search_terms)
        if query_matches:
            print(f'{query_matches}')
            print(f'---------------')
            print(f'{text}\n')


if __name__ == '__main__':
    main()
