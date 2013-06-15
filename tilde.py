# -*- coding=UTF-8 -*-

from __future__ import unicode_literals

from goldendict_reader import GoldenDictReader


class GoldenDictTildeProcessor(GoldenDictReader):

    def _procces_tilde(self, x):
        text = x['text'].replace('~', x['name'])
        return {
            'name': x['name'],
            'text': text,
        }

    def process(self, articles):

        articles = [self._procces_tilde(x) for x in articles]

        return articles

if __name__ == '__main__':
    import sys
    GoldenDictTildeProcessor()(sys.argv)
