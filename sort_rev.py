# -*- coding=UTF-8 -*-
import sys
import re

if len(sys.argv) != 2:
	print u'Ошибка: должен быть ровно один аргумент командной строки!'.encode('utf-8')
	exit(1)

#for arg in sys.argv:
#	print arg

filename = sys.argv[1].decode('utf-8')
try:
	f = open(filename, 'r')
except:
	print (u'Ошибка: невозможно открыть файл "%s"!' % filename).encode('utf-8')
	exit(1)

#for line in f:
#	line = line.decode('utf-8')
#	print (replaceref(line)).encode('utf-8'),

lines = []

for line in f:
	lines.append(line)

name = u''
text = u''

articles = []

header = []

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
			name = line.replace('\n','')
			text = u''
		else:
			text += line
		if i == len(lines) - 1:
			articles.append({
				'name': name,
				'text': text,
			})
# (),-.;
#АЙКЭабвгдежзийклмнопрстуфхцчшщъыьэюяёҥӓӧӱӹіӥӵӟӝ

alphabet = u'аӓбвгдеёжӝзӟиіӥйклмнҥоӧпрстуӱфхцчӵшщъыӹьэюяАӒБВГДЕЁЖӜЗӞИІӤЙКЛМНҤОӦПРСТУӰФХЦЧӴШЩЪЫӸЬЭЮЯ'
alphabet_dict = dict([(x, alphabet.index(x)) for x in alphabet])
articles = sorted(articles, key=lambda word: [alphabet_dict[c] for c in word['name'][::-1].replace(' ','').replace('(','').replace(')','').replace(',','').replace('-','').replace('.','').replace(';','')])

alphabet = u'аӓбвгдеёжӝзӟиіӥйклмнҥоӧпрстуӱфхцчӵшщъыӹьэюя'
alphabet_dict = dict([(x, alphabet.index(x)) for x in alphabet])
articles = sorted(articles, key=lambda word: [alphabet_dict[c] for c in word['name'][::-1].replace(' ','').replace('(','').replace(')','').replace(',','').replace('-','').replace('.','').replace(';','').lower()])

for h in header:
	print h.encode('utf-8'),

for a in articles:
	print a['name'].encode('utf-8')
	print a['text'].encode('utf-8'),
