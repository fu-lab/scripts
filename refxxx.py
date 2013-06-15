# -*- coding=UTF-8 -*-

from __future__ import unicode_literals

from goldendict_reader import GoldenDictReader

import re


class GoldenDictRefXXXProcessor(GoldenDictReader):

    def _procces_refxxx(self, x):
        remove_xxx = lambda x: x.replace('<xxx>', '').replace('</xxx>', '')
        result = x
        xxx = re.findall(r'<xxx>[^<]+<\/xxx>', x['text'])
        if len(xxx) == 1:
            if len(re.findall(r'"yyy"', x['text'])) == 1:
                xxx = remove_xxx(xxx[0])
                result['text'] = remove_xxx(
                    x['text'].replace('"yyy"', '"' + xxx + '"')
                )
        return result

    def process(self, articles):

        articles = [self._procces_refxxx(x) for x in articles]

        return articles

if __name__ == '__main__':
    import sys
    GoldenDictRefXXXProcessor()(sys.argv)
