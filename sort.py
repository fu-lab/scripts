# -*- coding=UTF-8 -*-

from __future__ import unicode_literals

from goldendict_reader import GoldenDictReader


class GoldenDictSorter(GoldenDictReader):

    def _sort(self, articles, is_lower=False):
        do_lower = lambda str, is_lower: str.lower() if is_lower else str
        alphabet = 'аӓбвгдеёжӝзӟиіӥйклмнҥоӧпрстуӱфхцчӵшщъыӹьэюя'
        if not is_lower:
            alphabet += alphabet.upper()
        alphabet_dict = dict([(x, alphabet.index(x)) for x in alphabet])

        def only_alphabet_chars(str, alphabet):
            for letter in str:
                if not letter in alphabet:
                    str = str.replace(letter, '')
            return str

        articles = sorted(
            articles,
            key=lambda word: [
                alphabet_dict[c] for c in only_alphabet_chars(
                    do_lower(
                        word['name'],
                        is_lower
                    ),
                    alphabet
                )
            ]
        )
        return articles

    def process(self, articles):

        '''
        alphabet = 'аӓбвгдеёжӝзӟиіӥйклмнҥоӧпрстуӱфхцчӵшщъыӹьэюя'
        alphabet_dict = dict([(x, alphabet.index(x)) for x in alphabet])

        articles = sorted(
            articles,
            key=lambda word: [
                alphabet_dict[c] for c in remove_chars(
                    word['name'], ' (),-.;').lower()
            ])
        '''

        articles = self._sort(articles, False)
        articles = self._sort(articles, True)

        return articles

if __name__ == '__main__':
    import sys
    GoldenDictSorter()(sys.argv)
