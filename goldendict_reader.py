# -*- coding=UTF-8 -*-

from __future__ import unicode_literals

import sys


remove_chars = lambda str, chars: str if not len(
    chars) else remove_chars(str.replace(chars[0], ''), chars[1:])


class GoldenDictReader(object):

    def parse_file(self, lines):
        header = []
        articles = []
        name = ''
        text = ''
        for i in range(len(lines)):
            line = lines[i]
            line = line.decode('utf-8')
            if line[0] == '#':
                header.append(line)
            else:
                if line[0] != '\t':
                    # начинаем новую статью
                    if name != '':
                        articles.append({
                            'name': name,
                            'text': text,
                        })
                    name = line.replace('\n', '')
                    text = ''
                else:
                    text += line
                if i == len(lines) - 1:
                    articles.append({
                        'name': name,
                        'text': text,
                    })
        return (header, articles, )

    def read_file(self, argv, stderr=sys.stderr):
        if len(argv) != 2:
            stderr.write('Ошибка: должен быть ровно один аргумент '
                         'командной строки!\n'.encode('utf-8'))
            exit(1)
        filename = argv[1].decode('utf-8')
        try:
            f = open(filename, 'r')
        except:
            stderr.write(('Ошибка: невозможно открыть '
                          'файл "%s"!\n' % filename).encode('utf-8'))
            exit(1)
        lines = []
        for line in f:
            lines.append(line)
        return lines

    def __call__(self, argv, stdout=sys.stdout, stderr=sys.stderr, *args,
                 **kwargs):
        lines = self.read_file(argv, stderr=stderr)
        header, articles = self.parse_file(lines)
        articles = self.process(articles)
        self.print_result(header, articles, stdout=stdout)

    def process(self, articles):
        return articles

    def print_result(self, header, articles, stdout=sys.stdout):
        for h in header:
            stdout.write(h.encode('utf-8'))
        for a in articles:
            stdout.write((a['name'] + '\n').encode('utf-8'))
            stdout.write(a['text'].encode('utf-8'))

if __name__ == '__main__':
    GoldenDictReader()(sys.argv)
